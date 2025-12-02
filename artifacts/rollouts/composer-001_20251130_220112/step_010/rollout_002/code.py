
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

# Marcus: Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=49, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=49, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=49, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25),  # Bb7
    pretty_midi.Note(velocity=100, pitch=53, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.0, end=4.25),  # Bb7
    pretty_midi.Note(velocity=100, pitch=53, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=55, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=4.0, end=4.25),  # G
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat])

# Dante: Motif in F (start at 1.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
