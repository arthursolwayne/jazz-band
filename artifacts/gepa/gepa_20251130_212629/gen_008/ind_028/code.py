
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
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

kick_times = [0.0, 1.5]
snare_times = [0.75, 2.25]
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no note repeated
bass_notes = [62, 63, 64, 65, 67, 69, 71, 72]
bass_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: G7 (G B D F)
    71, 76, 69, 67,
    # Bar 2, beat 4: C7 (C E G B)
    60, 64, 67, 71,
    # Bar 3, beat 2: F7 (F A C E)
    65, 70, 60, 64,
    # Bar 3, beat 4: G7 again
    71, 76, 69, 67,
    # Bar 4, beat 2: C7 again
    60, 64, 67, 71,
    # Bar 4, beat 4: D7 (D F# A C#)
    62, 67, 69, 73
]
piano_times = [
    2.25, 2.375, 2.5, 2.625,
    3.0, 3.125, 3.25, 3.375,
    3.75, 3.875, 4.0, 4.125,
    4.5, 4.625, 4.75, 4.875,
    5.25, 5.375, 5.5, 5.625
]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125))

# Sax: motif in D minor, short, singable
# Phrase: D - F - G - D (hanging)
sax_notes = [62, 64, 67, 62]
sax_times = [1.5, 1.875, 2.25, 2.625]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Repeat the motif at bar 3, 0.5 seconds later
sax_notes = [62, 64, 67, 62]
sax_times = [3.0, 3.375, 3.75, 4.125]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Final motif at bar 4, 0.5 seconds later
sax_notes = [62, 64, 67, 62]
sax_times = [4.5, 4.875, 5.25, 5.625]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42] * 16

kick_times = [1.5, 3.0, 4.5, 6.0]
snare_times = [2.25, 3.75, 5.25, 6.75]
hihat_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625, 6.0, 6.375, 6.75, 7.125]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
