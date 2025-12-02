
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=75, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),  # Ab
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),  # Bb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s): F7
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # E
    # Bar 3 (3.0 - 4.5s): Bb7
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # E
    # Bar 4 (4.5 - 6.0s): F7
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.6875, end=1.875), # Bb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.1875, end=3.375), # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5625), # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.0625), # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=5.0625, end=5.25), # F
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.4375), # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=5.4375, end=5.625), # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=5.8125), # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3
kick_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=36, start=5.8125, end=6.0)
]
for note in kick_notes:
    drums.notes.append(note)

# Snare on 2 and 4
snare_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75)
]
for note in snare_notes:
    drums.notes.append(note)

# Hi-hat on every eighth
hihat_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
for note in hihat_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
