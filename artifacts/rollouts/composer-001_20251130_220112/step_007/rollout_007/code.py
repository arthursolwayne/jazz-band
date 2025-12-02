
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: Fm7 (F, Ab, D, C)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=4.125, end=4.5),  # Eb
    # Bar 4: Fm7 (F, Ab, D, C)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb) - comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625),  # Ab
    # Bar 3: Bb7 (Bb, D, F, Ab) - comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=4.125),  # Ab
    # Bar 4: Fm7 (F, Ab, C, Eb) - comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Play F (64) and Ab (61)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),
    # Bar 3: Leave it hanging (no note for now)
    # Bar 4: Come back and finish it with D (66) and C (60)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
