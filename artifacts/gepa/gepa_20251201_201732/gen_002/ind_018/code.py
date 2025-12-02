
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
for time in [0.0, 0.75, 1.5]:  # kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
for time in [0.375, 1.125]:  # snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125))
for time in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]:  # hihat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.0625))
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = []
time = 1.5
bass_notes.append(pretty_midi.Note(velocity=80, pitch=53, start=time, end=time + 0.375))  # F
bass_notes.append(pretty_midi.Note(velocity=80, pitch=54, start=time + 0.375, end=time + 0.75))  # F#
bass_notes.append(pretty_midi.Note(velocity=80, pitch=55, start=time + 0.75, end=time + 1.125))  # G
bass_notes.append(pretty_midi.Note(velocity=80, pitch=57, start=time + 1.125, end=time + 1.5))  # A
time += 1.5
bass_notes.append(pretty_midi.Note(velocity=80, pitch=57, start=time, end=time + 0.375))  # A
bass_notes.append(pretty_midi.Note(velocity=80, pitch=58, start=time + 0.375, end=time + 0.75))  # A#
bass_notes.append(pretty_midi.Note(velocity=80, pitch=59, start=time + 0.75, end=time + 1.125))  # B
bass_notes.append(pretty_midi.Note(velocity=80, pitch=60, start=time + 1.125, end=time + 1.5))  # C
time += 1.5
bass_notes.append(pretty_midi.Note(velocity=80, pitch=60, start=time, end=time + 0.375))  # C
bass_notes.append(pretty_midi.Note(velocity=80, pitch=61, start=time + 0.375, end=time + 0.75))  # C#
bass_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=time + 0.75, end=time + 1.125))  # D
bass_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=time + 1.125, end=time + 1.5))  # E
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = []
def add_chord(root, time):
    chord = [root, root + 7, root + 12, root + 19]
    for pitch in chord:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375))
add_chord(53, 1.5)  # Fmaj7
add_chord(55, 3.0)  # G7
add_chord(57, 4.5)  # Am7
add_chord(60, 6.0)  # Cmaj7
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
# Bar 2: Start motif (F, G, A)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=55, start=1.75, end=2.0))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=57, start=2.0, end=2.25))
# Bar 3: Leave it hanging
sax_notes.append(pretty_midi.Note(velocity=110, pitch=57, start=2.25, end=2.5))
# Bar 4: Come back and finish it
sax_notes.append(pretty_midi.Note(velocity=110, pitch=55, start=3.0, end=3.25))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=53, start=3.25, end=3.5))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=55, start=3.5, end=3.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=57, start=3.75, end=4.0))
# End the motif with a return to the first note
sax_notes.append(pretty_midi.Note(velocity=110, pitch=53, start=4.0, end=4.25))
sax.notes.extend(sax_notes)

# Drums for Bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    for time in [start_time, start_time + 1.5]:  # kick on 1 and 3
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    for time in [start_time + 0.75, start_time + 1.125]:  # snare on 2 and 4
        drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125))
    for time in [start_time + i * 0.375 for i in range(4)]:  # hihat on every eighth
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.0625))
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.1875, end=time + 0.25))
add_drums(1.5)
add_drums(3.0)
add_drums(4.5)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
