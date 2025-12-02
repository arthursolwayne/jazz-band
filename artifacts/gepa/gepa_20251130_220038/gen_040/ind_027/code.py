
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
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Diane
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875)
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
for beat in [1.5, 2.25, 3.0, 3.75, 4.5, 5.25]:
    drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=beat, end=beat + 0.375)
    drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=beat + 0.75, end=beat + 1.125)
    drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=beat, end=beat + 0.75)
    drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Sax: Dante - the melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
