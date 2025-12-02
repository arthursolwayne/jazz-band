
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42] * 8

kick_times = [0.0, 0.75, 1.5, 2.25]
snare_times = [0.375, 1.125, 1.875, 2.625]
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]

for note, time in zip(kick_notes, kick_times):
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

for note, time in zip(snare_notes, snare_times):
    note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

for note, time in zip(hihat_notes, hihat_times):
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 71, 70, 69]
bass_times = [1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25]

for note, time in zip(bass_notes, bass_times):
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
chord_notes = [
    [60, 64, 67, 71],  # C7
    [60, 64, 67, 71],  # C7
    [60, 64, 67, 71],  # C7
    [60, 64, 67, 71],  # C7
    [62, 66, 69, 73],  # D7
    [62, 66, 69, 73],  # D7
    [62, 66, 69, 73],  # D7
    [62, 66, 69, 73],  # D7
    [64, 68, 71, 75],  # E7
    [64, 68, 71, 75],  # E7
    [64, 68, 71, 75],  # E7
    [64, 68, 71, 75],  # E7
    [60, 64, 67, 71],  # C7
    [60, 64, 67, 71],  # C7
    [60, 64, 67, 71],  # C7
    [60, 64, 67, 71],  # C7
]

chord_times = [
    1.75, 1.75, 1.75, 1.75,
    2.25, 2.25, 2.25, 2.25,
    2.75, 2.75, 2.75, 2.75,
    3.25, 3.25, 3.25, 3.25
]

for notes, time in zip(chord_notes, chord_times):
    for pitch in notes:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
        piano.notes.append(note)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [62, 64, 65, 64, 62, 60, 62, 64]
sax_times = [1.5, 1.75, 2.0, 2.25, 3.5, 3.75, 4.0, 4.25]

for note, time in zip(sax_notes, sax_times):
    note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
