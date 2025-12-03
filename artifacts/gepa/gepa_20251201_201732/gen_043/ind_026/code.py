
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25), # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0)   # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875), # C5
]
# Bar 3: Bb7 (tritone substitution)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625), # E5
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625), # G5
])
# Bar 4: G7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # B4
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=3.0),  # C5
    pretty_midi.Note(velocity=90, pitch=81, start=2.625, end=3.0),  # D5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D (62), Eb (63), F (65), G (67), A (69), Bb (71), B (72), C (72)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0)   # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern as bar 1, shifted by 1.5s
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend(drum_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Same pattern as bar 1, shifted by 3.0s
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend(drum_notes)

# Bar 3: Bass (3.0 - 4.5s)
# Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5)   # D2 (root)
]
bass.notes.extend(bass_notes)

# Bar 4: Bass (4.5 - 6.0s)
# Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25), # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0)   # D2 (root)
]
bass.notes.extend(bass_notes)

# Bar 3: Piano (3.0 - 4.5s)
# Dm7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375), # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375), # C5
]
piano.notes.extend(piano_notes)

# Bar 4: Piano (4.5 - 6.0s)
# G7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.875),  # D5
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
