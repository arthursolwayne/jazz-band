
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: F - Bb - Eb - Ab (half note, half note, half note, half note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=3.0),
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=4.5),
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=6.0),
    pretty_midi.Note(velocity=110, pitch=58, start=6.0, end=7.5),
]

sax.notes.extend(sax_notes)

# Bass: Walking line in F (F - Gb - G - Ab - A - Bb - B - C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
# Bars 2-4: 7th chords on 2 and 4 (measures 2 and 4)
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, Db
# Ab7 = Ab, C, Eb, Gb
# All chords at beat 2 and 4 of bars 2-4

# Bar 2: F7 on 2 and 4
piano_notes = []
for beat in [2, 4]:
    start = 1.5 + (beat - 1) * 0.75
    # F7
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=74, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=77, start=start, end=start + 0.375))

# Bar 3: Bb7 on 2 and 4
for beat in [2, 4]:
    start = 3.0 + (beat - 1) * 0.75
    # Bb7
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=70, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=73, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=78, start=start, end=start + 0.375))

# Bar 4: Eb7 on 2 and 4
for beat in [2, 4]:
    start = 4.5 + (beat - 1) * 0.75
    # Eb7
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=74, start=start, end=start + 0.375))
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=75, start=start, end=start + 0.375))

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
