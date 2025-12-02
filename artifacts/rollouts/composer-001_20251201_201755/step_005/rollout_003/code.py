
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=2.0),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=2.0, end=2.5),  # F2
    pretty_midi.Note(velocity=100, pitch=41, start=2.5, end=3.0),  # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.5),  # G2
    pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=4.0),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=4.0, end=4.5),  # F#2
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=5.0),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.5),  # D2
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=6.0),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: Dmaj7 (D, F#, A, C#) in open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C#4
]

# Bar 3: G7 (G, B, D, F) in open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # F4
])

# Bar 4: Cmaj7 (C, E, G, B) in open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # B4
])

# Add resolving chords on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # D4
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (One short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
# Motif: D4 (start bar 2), F4 (end bar 2), G4 (start bar 3), D4 (end bar 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
