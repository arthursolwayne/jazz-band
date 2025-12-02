
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)

drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=73, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=75, start=5.625, end=6.0),
]

bass.notes.extend(bass_notes)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
]

piano.notes.extend(piano_notes)

# Little Ray on drums (1.5 - 6.0s)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25)
hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)
hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)
hihat13 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
hihat14 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
hihat15 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)

kick3 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)

drums.notes.extend([kick2, snare2, hihat5, hihat6, hihat7, hihat8, hihat9, hihat10, hihat11, hihat12, hihat13, hihat14, hihat15, kick3, snare3, kick4, snare4])

# Dante on sax - one short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
