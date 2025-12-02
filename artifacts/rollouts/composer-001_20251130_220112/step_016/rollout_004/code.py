
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
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice.
# D minor key: D, Eb, F, G, Ab, Bb, B, C
bass_notes = [62, 60, 63, 62, 60, 59, 60, 62, 63, 62, 60, 59, 60, 62, 63, 64]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb

# Bar 2 (1.5 - 3.0s)
# Dm7 on 2 and 4
piano_notes = [62, 65, 67, 69]  # Dm7
for i in range(2):
    start = 1.5 + 0.75 + i * 1.5
    for note in piano_notes:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
        piano.notes.append(piano_note)

# Bar 3 (3.0 - 4.5s)
# G7 on 2 and 4
piano_notes = [67, 71, 69, 65]  # G7
for i in range(2):
    start = 3.0 + 0.75 + i * 1.5
    for note in piano_notes:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
        piano.notes.append(piano_note)

# Bar 4 (4.5 - 6.0s)
# Cm7 on 2 and 4
piano_notes = [60, 64, 67, 71]  # Cm7
for i in range(2):
    start = 4.5 + 0.75 + i * 1.5
    for note in piano_notes:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
        piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D - F - Ab - Bb (D minor)
# Motif: D (62), F (65), Ab (68), Bb (71)
# Play the first two notes, leave the last two for the next bar
sax_notes = [62, 65, 68, 71]
for i, note in enumerate(sax_notes[:2]):
    start = 1.5 + i * 0.375
    end = start + 0.375
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(sax_note)

# Play the last two notes in bar 3
for i, note in enumerate(sax_notes[2:]):
    start = 3.0 + i * 0.375
    end = start + 0.375
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(sax_note)

# Drums: Bar 2-4
for bar in range(2, 5):
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
