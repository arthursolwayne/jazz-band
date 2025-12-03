
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Cm7 (F, Ab, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),  # C4
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=2.0),  # Ab3
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=2.0),  # Bb3
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.0),  # D4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25), # B4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=3.0),  # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # Eb2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # G2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (F, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # F4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.5),  # Bb3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.5),  # F4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75), # B4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125), # A4
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),  # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),  # C4
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=5.0),  # E4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25), # B4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # A4
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0),  # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
