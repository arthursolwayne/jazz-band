
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeating notes
# Dm7 chord: D F A C
# Bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [50, 51, 52, 53, 55, 56, 57, 58, 50]
for i in range(3):  # 3 bars
    for j in range(4):  # 4 beats per bar
        note = bass_notes[i * 4 + j]
        start = 1.5 + i * 1.5 + j * 0.375
        end = start + 0.375
        bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# Dm7: D F A C
# Comp on beats 2 and 4
for bar in range(3):  # 3 bars
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 1 or beat == 3:
            # Dm7 chord: D F A C
            for note in [50, 53, 57, 60]:
                piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, B, C
# Motif: D -> Eb -> F -> A (3 notes), then rest, then D -> Eb -> F -> A
# First iteration: start on beat 1 of bar 2
for i in range(2):  # play motif twice
    for note, offset in zip([50, 51, 52, 57], [0, 0.375, 0.75, 1.125]):
        start = 1.5 + i * 2.25 + offset
        sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25))

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
