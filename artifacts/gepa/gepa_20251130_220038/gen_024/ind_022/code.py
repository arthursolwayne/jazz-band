
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

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    kick_notes = [36] * 2  # Kick on beats 1 and 3
    snare_notes = [38] * 2  # Snare on beats 2 and 4
    hihat_notes = [42] * 8  # Hihat on every eighth note
    
    for i, note in enumerate(kick_notes):
        time = start + (i * 0.75)
        kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
        drums.notes.append(kick)
    
    for i, note in enumerate(snare_notes):
        time = start + (i * 0.75) + 0.375
        snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
        drums.notes.append(snare)
    
    for i, note in enumerate(hihat_notes):
        time = start + (i * 0.375)
        hihat = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1875)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# F7 chord: F, A, C, E
# Bass line: F - G - A - Bb - B - C - D - Eb - E - F# - G - A - Bb - B - C - D

bass_notes = [71, 72, 74, 73, 76, 72, 74, 71, 76, 77, 74, 76, 73, 76, 72, 74]
bass_velocities = [80] * len(bass_notes)

for i, note in enumerate(bass_notes):
    time = 1.5 + (i * 0.375)
    bass_note = pretty_midi.Note(velocity=bass_velocities[i], pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
# F7 on beat 1, A7 on beat 2, C7 on beat 3, E7 on beat 4
# Repeat this pattern
chords = [
    [57, 60, 64, 67],  # F7
    [60, 64, 67, 71],  # A7
    [64, 67, 71, 72],  # C7
    [67, 71, 72, 76],  # E7
]

for bar in range(3):  # Bars 2-4
    for i, chord in enumerate(chords):
        time = 1.5 + (bar * 1.5) + (i * 0.75)
        for note in chord:
            piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
            piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - Bb - F (melodic interval, not scale)
# Play on beat 1 of bar 2, then leave it open, return on beat 3 of bar 4 to finish

sax_notes = [65, 67, 69, 65, 67, 69, 65]
sax_durations = [0.375, 0.375, 0.375, 0.1875, 0.375, 0.375, 0.375]
sax_velocities = [105, 105, 100, 105, 105, 105, 105]

for i, note in enumerate(sax_notes):
    if i == 3:
        # Leave it hanging
        time = 1.5 + (0 * 1.5) + (0 * 0.75) + 0.375 * 3
        sax_note = pretty_midi.Note(velocity=sax_velocities[i], pitch=note, start=time, end=time + 0.1875)
        sax.notes.append(sax_note)
    else:
        time = 1.5 + (0 * 1.5) + (0 * 0.75) + sax_durations[i] * i
        sax_note = pretty_midi.Note(velocity=sax_velocities[i], pitch=note, start=time, end=time + sax_durations[i])
        sax.notes.append(sax_note)

# Finish the motif on beat 3 of bar 4
sax_notes = [67, 69, 65]
sax_durations = [0.375, 0.375, 0.375]
for i, note in enumerate(sax_notes):
    time = 1.5 + (3 * 1.5) + (2 * 0.75) + sax_durations[i] * i
    sax_note = pretty_midi.Note(velocity=sax_velocities[i], pitch=note, start=time, end=time + sax_durations[i])
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
