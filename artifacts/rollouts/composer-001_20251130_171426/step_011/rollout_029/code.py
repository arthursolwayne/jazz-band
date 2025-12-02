
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
for bar in range(1):
    start = bar * bar_length
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for beat in range(8):
        note = pretty_midi.Note(velocity=90, pitch=42, start=start + beat * 0.1875, end=start + beat * 0.1875 + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Dm, chromatic approaches
bass_notes = [
    50, 49, 51, 53,  # Dm7
    53, 51, 50, 49,  # Dm7
    50, 49, 51, 53,  # Dm7
    53, 51, 50, 49   # Dm7
]
for i, note in enumerate(bass_notes):
    start = 1.5 + (i // 4) * bar_length + (i % 4) * 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(bass_note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    62, 67, 60, 64,  # Dm7 on 2 and 4
    # Bar 3
    62, 67, 60, 64,
    # Bar 4
    62, 67, 60, 64
]
for i, note in enumerate(piano_notes):
    start = 1.5 + (i // 4) * bar_length + (i % 4) * 0.375
    piano_note = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(piano_note)

# Sax - one short motif, make it sing
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, G, D (with chromatic passing)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.5 + 0.125),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5 + 0.125, end=1.5 + 0.25),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5 + 0.25, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5 + 0.375, end=1.5 + 0.5)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * bar_length
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for beat in range(8):
        note = pretty_midi.Note(velocity=90, pitch=42, start=start + beat * 0.1875, end=start + beat * 0.1875 + 0.05)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save("dante_intro.mid")
