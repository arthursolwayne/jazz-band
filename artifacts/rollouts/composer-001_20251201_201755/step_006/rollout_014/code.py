
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
drum_notes = []
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Dm, roots and fifths, chromatic approaches
bass_notes = []
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    if bar == 2:
        # Dm -> D, A
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=start, end=start + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=41, start=start + 0.75, end=start + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=start + 1.125, end=start + 1.5))
    elif bar == 3:
        # F -> F, C
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=46, start=start, end=start + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=45, start=start + 0.375, end=start + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=44, start=start + 0.75, end=start + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=46, start=start + 1.125, end=start + 1.5))
    elif bar == 4:
        # Bb -> Bb, F
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=41, start=start, end=start + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=40, start=start + 0.375, end=start + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=39, start=start + 0.75, end=start + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=41, start=start + 1.125, end=start + 1.5))
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last beat of each bar
piano_notes = []
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    if bar == 2:
        # Dm7: D, F, A, C
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=43, start=start, end=start + 0.375))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=46, start=start, end=start + 0.375))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=45, start=start, end=start + 0.375))
    elif bar == 3:
        # F7: F, A, C, Eb
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=46, start=start + 0.375, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=49, start=start + 0.375, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=45, start=start + 0.375, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=48, start=start + 0.375, end=start + 0.75))
    elif bar == 4:
        # Bb7: Bb, D, F, Ab
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=41, start=start + 1.125, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=44, start=start + 1.125, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=40, start=start + 1.125, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=43, start=start + 1.125, end=start + 1.5))
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
bar = 2
start = (bar - 1) * 1.5
# Begin motif on beat 1 of bar 2
sax_notes.append(pretty_midi.Note(velocity=110, pitch=49, start=start, end=start + 0.375))  # E
sax_notes.append(pretty_midi.Note(velocity=110, pitch=47, start=start + 0.375, end=start + 0.75))  # D
sax_notes.append(pretty_midi.Note(velocity=110, pitch=49, start=start + 0.75, end=start + 1.125))  # E
sax_notes.append(pretty_midi.Note(velocity=110, pitch=51, start=start + 1.125, end=start + 1.5))  # G
sax_notes.append(pretty_midi.Note(velocity=110, pitch=49, start=start + 1.5, end=start + 1.875))  # E
sax_notes.append(pretty_midi.Note(velocity=110, pitch=47, start=start + 1.875, end=start + 2.25))  # D
sax_notes.append(pretty_midi.Note(velocity=110, pitch=49, start=start + 2.25, end=start + 2.625))  # E
sax_notes.append(pretty_midi.Note(velocity=110, pitch=51, start=start + 2.625, end=start + 3.0))  # G
sax_notes.append(pretty_midi.Note(velocity=110, pitch=50, start=start + 3.0, end=start + 3.375))  # F
sax_notes.append(pretty_midi.Note(velocity=110, pitch=49, start=start + 3.375, end=start + 3.75))  # E
sax_notes.append(pretty_midi.Note(velocity=110, pitch=47, start=start + 3.75, end=start + 4.125))  # D
sax_notes.append(pretty_midi.Note(velocity=110, pitch=45, start=start + 4.125, end=start + 4.5))  # C
sax_notes.append(pretty_midi.Note(velocity=110, pitch=47, start=start + 4.5, end=start + 4.875))  # D
sax_notes.append(pretty_midi.Note(velocity=110, pitch=49, start=start + 4.875, end=start + 5.25))  # E
sax_notes.append(pretty_midi.Note(velocity=110, pitch=51, start=start + 5.25, end=start + 5.625))  # G
sax_notes.append(pretty_midi.Note(velocity=110, pitch=50, start=start + 5.625, end=start + 6.0))  # F

sax.notes.extend(sax_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
