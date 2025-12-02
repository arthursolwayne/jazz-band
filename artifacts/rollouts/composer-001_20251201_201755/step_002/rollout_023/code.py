
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
bar_length = 1.5
time = 0.0
for beat in range(4):
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.375))
    time += 0.375

# Bars 2-4 (1.5 - 6.0s)

# Bar 2 (1.5 - 3.0s)
# Marcus: D2 (root), F2 (fifth), chromatic approach to D2
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))

# Diane: Open voicings, Dm7 (D-F-A-C), Bb7 (Bb-D-F-A), Gm7 (G-Bb-D-F), C7 (C-E-G-B)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875))

piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625))

piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0))

# Bar 3 (3.0 - 4.5s)
# Marcus: D2 (root), F2 (fifth), chromatic approach to D2
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=3.75, end=4.125))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))

# Diane: Open voicings, Dm7 (D-F-A-C), Bb7 (Bb-D-F-A), Gm7 (G-Bb-D-F), C7 (C-E-G-B)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375))

piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75))

piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125))

# Bar 4 (4.5 - 6.0s)
# Marcus: D2 (root), F2 (fifth), chromatic approach to D2
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))

# Diane: Open voicings, Dm7 (D-F-A-C), Bb7 (Bb-D-F-A), Gm7 (G-Bb-D-F), C7 (C-E-G-B)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875))

piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25))

piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625))

# Dante's sax motif: short, singable, leaves a question
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Motif: D, F, G, Bb (with slight syncopation)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5))

# Repeat the motif an octave higher with a slight delay
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=2.75, end=3.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=79, start=3.25, end=3.5))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=78, start=3.5, end=3.75))

# Add a final note, D, to give it closure
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.0))

# Drums for bars 2-4
for bar in range(2, 5):
    time_start = bar * bar_length - 1.5
    for beat in range(4):
        if beat % 2 == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time_start + beat * 0.375, end=time_start + beat * 0.375 + 0.375))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time_start + beat * 0.375, end=time_start + beat * 0.375 + 0.375))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time_start + beat * 0.375, end=time_start + beat * 0.375 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
