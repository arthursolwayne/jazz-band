
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, no repeated notes
# F7 scale: F, G, Ab, A, Bb, B, C, Db
bass_notes = [
    71,  # F (1st beat)
    72,  # G (2nd beat)
    70,  # Eb (3rd beat)
    71,  # F (4th beat)
    73,  # G# (1st beat)
    74,  # A (2nd beat)
    72,  # G (3rd beat)
    73,  # G# (4th beat)
    74,  # A (1st beat)
    75,  # Bb (2nd beat)
    73,  # G# (3rd beat)
    74,  # A (4th beat)
    75,  # Bb (1st beat)
    76,  # B (2nd beat)
    74,  # A (3rd beat)
    75,  # Bb (4th beat)
]

bass_times = [
    1.5, 1.875, 2.25, 2.625,
    3.0, 3.375, 3.75, 4.125,
    4.5, 4.875, 5.25, 5.625,
    6.0, 6.375, 6.75, 7.125
]

for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1))

# Diane on piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab
piano_notes = [
    65, 68, 69, 67,  # F7 on beat 2
    67, 70, 69, 68,  # Bb7 on beat 4
    65, 68, 69, 67,  # F7 on beat 2
    67, 70, 69, 68,  # Bb7 on beat 4
    65, 68, 69, 67,  # F7 on beat 2
    67, 70, 69, 68   # Bb7 on beat 4
]

piano_times = [
    1.875, 2.125, 2.375, 2.625,
    3.375, 3.625, 3.875, 4.125,
    4.875, 5.125, 5.375, 5.625,
    6.375, 6.625, 6.875, 7.125
]

for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

kick_times = [1.5, 3.0]
snare_times = [2.25, 3.75]
hihat_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05))

# Bar 3 (3.0 - 4.5s)
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

kick_times = [3.0, 4.5]
snare_times = [3.75, 5.25]
hihat_times = [3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05))

# Bar 4 (4.5 - 6.0s)
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

kick_times = [4.5, 6.0]
snare_times = [5.25, 6.75]
hihat_times = [4.5, 4.875, 5.25, 5.625, 6.0, 6.375, 6.75, 7.125]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05))

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F minor blues scale: F, Gb, G, Ab, Bb, B
# Motif: F, Gb, Bb, B, F
# Play on beat 2 of bar 2, then on beat 4 of bar 4
sax_notes = [71, 70, 67, 68, 71]
sax_times = [2.25, 2.625, 3.0, 3.375, 3.75]

for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

# Repeat the motif on beat 4 of bar 4
sax_notes = [71, 70, 67, 68, 71]
sax_times = [5.625, 6.0, 6.375, 6.75, 7.125]

for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
