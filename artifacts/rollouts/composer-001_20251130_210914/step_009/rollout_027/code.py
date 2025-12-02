
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4])

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in F
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=54, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=56, start=4.875, end=5.25),  # G#
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane - 7th chords, comp on 2 and 4
# Bar 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Dante - Sax melody in F
# Motif: F - Bb - C - D - F (but leave it hanging on D at the end of bar 2)

sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

def fill_bar(start_time):
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125)
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    return [kick1, snare1, hihat1, hihat2, hihat3, hihat4]

drums.notes.extend(fill_bar(1.5))
drums.notes.extend(fill_bar(3.0))
drums.notes.extend(fill_bar(4.5))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
