
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
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Marcus: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=54, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=51, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=2.75, end=3.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Bar 2, beat 2: Fm7
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # D
]
# Bar 2, beat 4: Fm7
diane_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # D
])
piano.notes.extend(diane_notes)

# Bar 2, sax: Motif 1 (F, Ab, Bb, D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=84, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=81, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=82, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=86, start=1.875, end=2.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s)
# Marcus: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=51, start=4.25, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Bar 3, beat 2: Fm7
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # D
]
# Bar 3, beat 4: Fm7
diane_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # D
])
piano.notes.extend(diane_notes)

# Bar 3, sax: Motif 2 (F, Eb, D, E)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=84, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=81, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=82, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=85, start=3.375, end=3.5),  # E
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s)
# Marcus: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=54, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=5.75, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Bar 4, beat 2: Fm7
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # D
]
# Bar 4, beat 4: Fm7
diane_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=6.25, end=6.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=6.25, end=6.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=6.25, end=6.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=6.25, end=6.5),  # D
])
piano.notes.extend(diane_notes)

# Bar 4, sax: Motif 3 (F, Ab, Bb, D) - repeat motif 1
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=84, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=81, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=82, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=86, start=4.875, end=5.0),  # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
