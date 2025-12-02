
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
    start = bar * 1.5
    kick_notes = [36, 36]
    snare_notes = [38, 38]
    hihat_notes = [42] * 8
    kick_times = [start + 0.0, start + 0.75]
    snare_times = [start + 0.375, start + 1.125]
    hihat_times = [start + 0.0, start + 0.375, start + 0.75, start + 1.125,
                   start + 1.5, start + 1.875, start + 2.25, start + 2.625]

    for note, time in zip(kick_notes, kick_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(note_obj)
    for note, time in zip(snare_notes, snare_times):
        note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(note_obj)
    for note, time in zip(hihat_notes, hihat_times):
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line, chromatic approaches, never the same note twice
# F7 = F A C E
# Start on F, walk up and down, chromatic approach to F

bass_notes = [
    71, 73, 72, 71,  # F, G#, G, F (chromatic approach)
    71, 73, 72, 71,  # F, G#, G, F
    71, 73, 72, 71,  # F, G#, G, F
    71, 73, 72, 71,  # F, G#, G, F
]

bass_times = [1.5 + i * 0.375 for i in range(len(bass_notes))]

for pitch, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: Diane - 7th chords, comp on 2 and 4
# F7 = F A C E
# Play on 2 and 4 of each bar
piano_notes = [
    # Bar 2
    64, 69, 60, 67,  # F, A, C, E
    # Bar 3
    64, 69, 60, 67,  # F, A, C, E
    # Bar 4
    64, 69, 60, 67,  # F, A, C, E
]

piano_times = [2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875]

for pitch, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax: Dante - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F E D C
# Start on bar 2.5 (1.5 + 1.0), play F E D, then repeat C on bar 4
sax_notes = [
    65, 64, 62, 60,  # F E D C
    60, 62, 64, 65   # C D E F
]

sax_times = [2.5, 2.875, 3.25, 3.625, 4.0, 4.375, 4.75, 5.125]

# Leave F E D hanging, then resolve with C D E F
for pitch, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    kick_notes = [36, 36]
    snare_notes = [38, 38]
    hihat_notes = [42] * 8
    kick_times = [start + 0.0, start + 0.75]
    snare_times = [start + 0.375, start + 1.125]
    hihat_times = [start + 0.0, start + 0.375, start + 0.75, start + 1.125,
                   start + 1.5, start + 1.875, start + 2.25, start + 2.625]

    for note, time in zip(kick_notes, kick_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(note_obj)
    for note, time in zip(snare_notes, snare_times):
        note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(note_obj)
    for note, time in zip(hihat_notes, hihat_times):
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
