
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
for beat in [0, 2]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.125))
for beat in [1, 3]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.125))
for beat in range(4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=beat * 0.375 + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, chromatic approaches, no repeating notes
# D Dorian: D E F# G A B C
bass_notes = [50, 52, 53, 55, 57, 59, 60, 58, 57, 55, 53, 52, 50, 49, 50, 52]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.25
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# D7 = D F# A C
# G7 = G B D F
# A7 = A C# E G
# Bm7 = B D F# A
piano_notes = []
# Bar 2
piano_notes.extend([50, 53, 57, 59])  # D7
# Bar 3
piano_notes.extend([67, 71, 69, 67])  # G7
# Bar 4
piano_notes.extend([65, 68, 72, 69])  # A7
for i, note in enumerate(piano_notes):
    start = 1.5 + ((i // 4) * 1.5) + ((i % 4) * 0.375)
    end = start + 0.125
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Sax: Short motif, start it, leave it hanging, come back and finish it
# D - F# - A - D (but with syncopation)
sax_notes = [50, 53, 57, 50]
sax_times = [1.5, 1.75, 2.0, 3.75]
for i, note in enumerate(sax_notes):
    start = sax_times[i]
    end = start + 0.125
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Drums continue for full 4 bars
for beat in range(8):
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375 + 1.5, end=beat * 0.375 + 1.625))
    if beat % 2 == 1:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375 + 1.5, end=beat * 0.375 + 1.625))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375 + 1.5, end=beat * 0.375 + 1.625))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
