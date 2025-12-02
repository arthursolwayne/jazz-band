
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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

kick_times = [0.0, 0.75]
snare_times = [0.375, 1.125]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.0625))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
bass_times = [1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25]

for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    64, 67, 71, 72,  # C7
    # Bar 3
    64, 67, 71, 72,  # C7
    # Bar 4
    64, 67, 71, 72   # C7
]
piano_times = [
    # Bar 2
    1.75, 1.75, 1.75, 1.75,
    # Bar 3
    3.25, 3.25, 3.25, 3.25,
    # Bar 4
    4.75, 4.75, 4.75, 4.75
]

for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Motif. Start it, leave it hanging. Come back and finish it.
# Motif: C4, E4, G4, A4
sax_notes = [60, 64, 67, 69]
sax_times = [1.5, 1.75, 2.0, 2.25]

for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Repeat motif at end of the phrase
sax_notes = [60, 64, 67, 69]
sax_times = [4.5, 4.75, 5.0, 5.25]

for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
