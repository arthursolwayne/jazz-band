
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [1.5, 3.0, 4.5]:
    drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar, end=bar + 0.375)
    drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=bar + 0.75, end=bar + 1.125)
    drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar, end=bar + 1.5)
    drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Dante on sax: motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
