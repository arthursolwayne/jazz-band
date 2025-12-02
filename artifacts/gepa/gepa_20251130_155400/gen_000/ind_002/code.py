
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
bar_length = 1.5  # seconds per bar
for bar in range(1):
    start = bar * bar_length
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Marcus - Walking bass line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),   # G#
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625),  # G#
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),   # Bb
]
bass.notes.extend(bass_notes)

# Diane - 7th chords, comp on 2 and 4
# Bar 2: D7 on beat 2
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25),  # C
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),
]
piano.notes.extend(diane_notes)

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * bar_length
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Dante - Motif: D (F#), G (Bb), A (C), D (F#)
# Start on beat 2 of bar 2
dante_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.125),  # F#
    pretty_midi.Note(velocity=110, pitch=74, start=2.125, end=2.25), # G
    pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.375), # Bb
    pretty_midi.Note(velocity=110, pitch=79, start=2.375, end=2.5),  # A
    pretty_midi.Note(velocity=110, pitch=81, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=2.75), # D
    pretty_midi.Note(velocity=110, pitch=72, start=2.75, end=2.875), # F#
]
sax.notes.extend(dante_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
