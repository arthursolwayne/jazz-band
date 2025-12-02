
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
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Bass line in D major: D - C# - B - A - G - F# - E - D
bass_notes = [2, 1, 10, 9, 7, 6, 4, 2]
bass_times = [1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25]
for i in range(len(bass_notes)):
    note = pretty_midi.Note(velocity=80, pitch=bass_notes[i] + 24, start=bass_times[i], end=bass_times[i] + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# D7: D, F#, A, C
# G7: G, B, D, F
# A7: A, C#, E, G
# D7: D, F#, A, C

# Bar 2 (1.5-2.5s)
diane_notes = [2, 6, 9, 11]
diane_times = [1.75, 1.75, 1.75, 1.75]
for i in range(len(diane_notes)):
    note = pretty_midi.Note(velocity=90, pitch=diane_notes[i] + 60, start=diane_times[i], end=diane_times[i] + 0.25)
    piano.notes.append(note)

# Bar 3 (2.5-3.5s)
diane_notes = [7, 11, 2, 5]
diane_times = [2.75, 2.75, 2.75, 2.75]
for i in range(len(diane_notes)):
    note = pretty_midi.Note(velocity=90, pitch=diane_notes[i] + 60, start=diane_times[i], end=diane_times[i] + 0.25)
    piano.notes.append(note)

# Bar 4 (3.5-4.5s)
diane_notes = [9, 13, 15, 10]
diane_times = [3.75, 3.75, 3.75, 3.75]
for i in range(len(diane_notes)):
    note = pretty_midi.Note(velocity=90, pitch=diane_notes[i] + 60, start=diane_times[i], end=diane_times[i] + 0.25)
    piano.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Sax in D: D, E, F#, G, A, B, C#, D
# Motif: D - E - F# (run into the next bar), then A - B - C# in the third bar
sax_notes = [2, 3, 5, 5, 7, 8, 10, 10]
sax_times = [1.5, 1.625, 1.75, 2.0, 2.25, 2.375, 2.5, 2.625]
for i in range(len(sax_notes)):
    note = pretty_midi.Note(velocity=110, pitch=sax_notes[i] + 62, start=sax_times[i], end=sax_times[i] + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
