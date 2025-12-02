
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
    # Bar 1 (0.0 - 1.5s)
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
# Bass: Marcus - walking line (roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.875),  # C (root) on 1
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # F (fifth) on 2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # Eb (chromatic) on 3
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # C (root) on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - open voicings, different chord each bar
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Fmaj7
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G (Fmaj7 9)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # C (Fmaj7 5)
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # E (Fmaj7 7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # G (Fmaj7 9)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Marcus - walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # G (chromatic) on 1
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # C (root) on 2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # F (fifth) on 3
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # Eb (chromatic) on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - open voicings
piano_notes = [
    # Bar 3 (3.0 - 4.5s) - F7
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # A (F7 3)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # C (F7 5)
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # D (F7 7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # A (F7 3)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Marcus - walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # C (root) on 1
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25), # F (fifth) on 2
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625), # Eb (chromatic) on 3
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # C (root) on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - open voicings
piano_notes = [
    # Bar 4 (4.5 - 6.0s) - Fmaj7
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G (Fmaj7 9)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # C (Fmaj7 5)
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # E (Fmaj7 7)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # G (Fmaj7 9)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")
