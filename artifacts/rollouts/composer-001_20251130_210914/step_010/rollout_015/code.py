
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in F, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),   # D

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=75, start=4.5, end=4.875),  # D#
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),   # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=2.0),  # B
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=2.0),  # E

    # Bar 3
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.5),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.5),  # B
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.5),  # E

    # Bar 4
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=5.0),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=5.0),  # B
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=5.0),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - motif in F, short and haunting
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G

    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # G

    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Drums continue in bars 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start_time = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    drums.notes.append(kick1)
    drums.notes.append(kick2)

    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    drums.notes.append(snare1)
    drums.notes.append(snare2)

    # Hi-hat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start_time + (i * 0.375), end=start_time + (i * 0.375) + 0.375)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
