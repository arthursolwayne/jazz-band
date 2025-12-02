
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

# Drum pattern for bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=1.5)      # Hihat on every eighth
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, roots and fifths with chromatic approaches
# D2 (D), F#2 (F#), A2 (A), C#3 (C#), D3 (D), etc.
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F#2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A2 (octave)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # C#3 (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # F#2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # A2 (octave)
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # C#3 (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # F#2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # A2 (octave)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # C#3 (chromatic)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, different chords each bar
# Bar 2: Dmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4 (root)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4 (fifth)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C#5 (major 7)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F#5 (major 3)
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: D7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4 (root)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A4 (fifth)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # C#5 (major 7)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # E5 (minor 7)
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4 (root)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # G4 (minor 3)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # C#5 (fifth)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F#5 (minor 7)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - C#5 - D4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # C#5
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D4 (return)
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # C#5
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.25),  # C#5
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),  # C#5
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),  # F#4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue pattern for bars 2-4
# Same kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for eighth in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=start + eighth * 0.375, end=start + (eighth + 1) * 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
