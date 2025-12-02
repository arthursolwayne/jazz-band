
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=110, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for beat in range(8):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + beat * 0.125, end=start + beat * 0.125 + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice. D minor scale: D, Eb, F, G, Ab, Bb, C
# Walking bass line in D minor
bass_notes = [50, 49, 51, 52, 50, 49, 51, 52, 50, 49, 51, 52, 50, 49, 51, 52]
for i, note in enumerate(bass_notes):
    start = 1.5 + (i // 4) * 1.5 + (i % 4) * 0.375
    duration = 0.375
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Diane: 7th chords, comp on 2 and 4
# D7, Bb7, G7, C7
chords = [
    [50, 53, 55, 57],  # D7
    [48, 51, 53, 56],  # Bb7
    [52, 55, 57, 59],  # G7
    [52, 56, 59, 61]   # C7
]
for bar in range(2, 5):
    start = bar * 1.5
    if bar % 2 == 0:
        # Comp on 2 and 4
        for i, chord in enumerate(chords):
            for note in chord:
                if i == 1 or i == 3:
                    pitch = note
                    duration = 0.375
                    piano_note = pretty_midi.Note(velocity=95, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + duration)
                    piano.notes.append(piano_note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=110, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for beat in range(8):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + beat * 0.125, end=start + beat * 0.125 + 0.05)
        drums.notes.append(note)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D, F, G, Ab (start at bar 2)
motif = [50, 52, 53, 54]
# First pass: bars 2, 2.5, 3
for i, note in enumerate(motif):
    start = 1.5 + i * 0.75
    duration = 0.375
    sax_note = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Second pass: bars 3, 3.5, 4
for i, note in enumerate(motif):
    start = 3.0 + i * 0.75
    duration = 0.375
    sax_note = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
