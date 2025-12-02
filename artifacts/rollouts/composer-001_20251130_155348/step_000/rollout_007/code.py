
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36, 36]
kick_times = [bar1_start + 0.0, bar1_start + 1.0]
snare_notes = [38, 38]
snare_times = [bar1_start + 0.5, bar1_start + 1.5]
hihat_notes = [42] * 8
hihat_times = [bar1_start + 0.0, bar1_start + 0.25, bar1_start + 0.5, bar1_start + 0.75,
               bar1_start + 1.0, bar1_start + 1.25, bar1_start + 1.5, bar1_start + 1.75]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Dm7: D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D (chromatic approach to D)
bass_notes = [50, 51, 52, 53, 55, 56, 57, 58, 50]
bass_times = [bar2_start + 0.0, bar2_start + 0.25, bar2_start + 0.5, bar2_start + 0.75,
              bar2_start + 1.0, bar2_start + 1.25, bar2_start + 1.5, bar2_start + 1.75,
              bar2_start + 2.0]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1))

# Piano: 7th chords, comp on 2 and 4
# Dm7: D F A C
# G7: G B D F
# Cm7: C Eb G Bb
# F7: F A C Eb
piano_notes = []
piano_times = []
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    if bar % 2 == 0:
        # Comp on 2 and 4
        # Dm7 on 2
        chord_notes = [50, 53, 55, 57]
        chord_times = [bar_start + 0.5, bar_start + 0.5, bar_start + 0.5, bar_start + 0.5]
        for note, time in zip(chord_notes, chord_times):
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1))
        # G7 on 4
        chord_notes = [67, 70, 72, 74]
        chord_times = [bar_start + 1.5, bar_start + 1.5, bar_start + 1.5, bar_start + 1.5]
        for note, time in zip(chord_notes, chord_times):
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1))
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 - D (50), F (53), A (55), C (57)
# Motif: D -> F -> A -> C -> D (first part)
# Then restate with a twist: F -> A -> C -> D -> F
sax_notes = [50, 53, 55, 57, 50, 53, 55, 57, 53, 55, 57, 50]
sax_times = [bar2_start + 0.0, bar2_start + 0.25, bar2_start + 0.5, bar2_start + 0.75,
             bar2_start + 1.0, bar2_start + 1.25, bar2_start + 1.5, bar2_start + 1.75,
             bar2_start + 2.0, bar2_start + 2.25, bar2_start + 2.5, bar2_start + 2.75]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Drums: Bar 2-4
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    kick_notes = [36, 36]
    kick_times = [bar_start + 0.0, bar_start + 1.0]
    snare_notes = [38, 38]
    snare_times = [bar_start + 0.5, bar_start + 1.5]
    hihat_notes = [42] * 8
    hihat_times = [bar_start + 0.0, bar_start + 0.25, bar_start + 0.5, bar_start + 0.75,
                   bar_start + 1.0, bar_start + 1.25, bar_start + 1.5, bar_start + 1.75]

    for note, time in zip(kick_notes, kick_times):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
    for note, time in zip(snare_notes, snare_times):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
    for note, time in zip(hihat_notes, hihat_times):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
