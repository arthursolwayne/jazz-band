
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

for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=90, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=90, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=95, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=95, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    (pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75)),  # D
    (pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0)),  # C
    (pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25)),  # Eb
    (pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5)),  # F
    # Bar 3
    (pretty_midi.Note(velocity=80, pitch=54, start=2.5, end=2.75)),  # G
    (pretty_midi.Note(velocity=80, pitch=53, start=2.75, end=3.0)),  # F#
    (pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.25)),  # A
    (pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.5)),  # D
    # Bar 4
    (pretty_midi.Note(velocity=80, pitch=49, start=3.5, end=3.75)),  # C
    (pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.0)),  # Eb
    (pretty_midi.Note(velocity=80, pitch=52, start=4.0, end=4.25)),  # F
    (pretty_midi.Note(velocity=80, pitch=54, start=4.25, end=4.5)),  # G
    # Bar 4 continuation
    (pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75)),  # F#
    (pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=5.0)),  # A
    (pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25)),  # D
    (pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.5)),  # C
    (pretty_midi.Note(velocity=80, pitch=51, start=5.5, end=5.75)),  # Eb
    (pretty_midi.Note(velocity=80, pitch=52, start=5.75, end=6.0)),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2 (beat 2)
    (pretty_midi.Note(velocity=85, pitch=62, start=1.75, end=2.0)),  # D7 (F#)
    (pretty_midi.Note(velocity=85, pitch=67, start=1.75, end=2.0)),  # D7 (A)
    (pretty_midi.Note(velocity=85, pitch=69, start=1.75, end=2.0)),  # D7 (C)
    # Bar 2 (beat 4)
    (pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.5)),  # D7 (F#)
    (pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5)),  # D7 (A)
    (pretty_midi.Note(velocity=85, pitch=69, start=2.25, end=2.5)),  # D7 (C)
    # Bar 3 (beat 2)
    (pretty_midi.Note(velocity=85, pitch=62, start=2.75, end=3.0)),  # D7 (F#)
    (pretty_midi.Note(velocity=85, pitch=67, start=2.75, end=3.0)),  # D7 (A)
    (pretty_midi.Note(velocity=85, pitch=69, start=2.75, end=3.0)),  # D7 (C)
    # Bar 3 (beat 4)
    (pretty_midi.Note(velocity=85, pitch=62, start=3.25, end=3.5)),  # D7 (F#)
    (pretty_midi.Note(velocity=85, pitch=67, start=3.25, end=3.5)),  # D7 (A)
    (pretty_midi.Note(velocity=85, pitch=69, start=3.25, end=3.5)),  # D7 (C)
    # Bar 4 (beat 2)
    (pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=4.0)),  # D7 (F#)
    (pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.0)),  # D7 (A)
    (pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.0)),  # D7 (C)
    # Bar 4 (beat 4)
    (pretty_midi.Note(velocity=85, pitch=62, start=4.25, end=4.5)),  # D7 (F#)
    (pretty_midi.Note(velocity=85, pitch=67, start=4.25, end=4.5)),  # D7 (A)
    (pretty_midi.Note(velocity=85, pitch=69, start=4.25, end=4.5)),  # D7 (C)
]
piano.notes.extend(piano_notes)

# Sax: Motif in Dm, one short phrase, leave it hanging, come back and finish it
# Motif: D - Eb - F - G (quarter notes), then repeat starting on Eb

# First iteration
sax_notes = [
    (pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)),  # D
    (pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25)),  # F
    (pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5)),  # G
]
# Second iteration (starting on Eb)
sax_notes.extend([
    (pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5)),  # F
    (pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75)),  # G
    (pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0)),  # D
])
# Third iteration (starting on F)
sax_notes.extend([
    (pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75)),  # F
    (pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0)),  # G
    (pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25)),  # D
    (pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5)),  # Eb
])
# Final resolution
sax_notes.extend([
    (pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75)),  # D
    (pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0)),  # Eb
])
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=90, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=90, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=95, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=95, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
