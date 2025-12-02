
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

for i in range(2):
    kick_time = 0.0 + i * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=kick_time, end=kick_time + 0.375)
    drums.notes.append(kick)

for i in range(2):
    snare_time = 0.75 + i * 1.5
    snare = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=snare_time, end=snare_time + 0.375)
    drums.notes.append(snare)

for i in range(8):
    hihat_time = 0.0 + i * 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.125)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line, chromatic approaches, no repeating notes
bass_notes = [
    50,  # D
    49,  # C
    51,  # Eb
    53,  # F
    55,  # G
    53,  # F
    51,  # Eb
    50,  # D
    49,  # C
    48,  # Bb
    50,  # D
    52,  # E
    55,  # G
    53,  # F
    51,  # Eb
    50   # D
]

for i, note in enumerate(bass_notes):
    time = 1.5 + i * 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    62, 64, 65, 67,  # Dm7 (D, F, A, C)
    62, 64, 65, 67,  # Dm7
    # Bar 3
    62, 64, 65, 67,
    62, 64, 65, 67,
    # Bar 4
    62, 64, 65, 67,
    62, 64, 65, 67
]

for i, note in enumerate(piano_notes):
    time = 1.5 + i * 0.375
    # Play on beats 2 and 4 only (i % 4 == 1 or i % 4 == 3)
    if (i % 4 == 1 or i % 4 == 3):
        piano_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
        piano.notes.append(piano_note)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (64), G (65), D (62) — but incomplete
sax_notes = [
    # Bar 2
    62, 64, 65, 62,
    # Bar 3
    62, 64, 65, 62,
    # Bar 4
    62, 64, 65, 62
]

for i, note in enumerate(sax_notes):
    time = 1.5 + i * 0.375
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
