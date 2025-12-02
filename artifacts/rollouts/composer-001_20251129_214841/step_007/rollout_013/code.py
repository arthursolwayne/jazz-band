
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42] * 8

for i in range(4):
    kick = pretty_midi.Note(velocity=80, pitch=kick_notes[i], start=i * 0.375, end=(i + 1) * 0.375)
    snare = pretty_midi.Note(velocity=80, pitch=snare_notes[i], start=(i + 1) * 0.375, end=(i + 2) * 0.375)
    drums.notes.append(kick)
    drums.notes.append(snare)

for i in range(8):
    hihat = pretty_midi.Note(velocity=60, pitch=hihat_notes[i], start=i * 0.1875, end=(i + 1) * 0.1875)
    drums.notes.append(hihat)

# Bars 2-4 (1.5 - 6.0s)
# Bass line: walking line, chromatic approaches
bass_notes = [
    64, 65, 67, 69,   # Bar 2
    71, 72, 74, 76,   # Bar 3
    77, 79, 81, 83    # Bar 4
]
for i, note in enumerate(bass_notes):
    start = 1.5 + (i % 4) * 0.375
    duration = 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2, E7 on beat 4
    (60, 64, 67, 71),  # C7
    (64, 67, 71, 74),  # E7
    # Bar 3: A7 on beat 2, D7 on beat 4
    (69, 72, 76, 79),  # A7
    (67, 71, 74, 77),  # D7
    # Bar 4: G7 on beat 2, C7 on beat 4
    (67, 71, 74, 79),  # G7
    (60, 64, 67, 71)   # C7
]
for i, chord in enumerate(piano_notes):
    beat = i % 4
    if beat == 1 or beat == 3:
        start = 1.5 + beat * 0.375
        for note in chord:
            piano_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.1875)
            piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C - E - B - D (Cmaj7), then repeat with a half-step chromatic approach
sax_notes = [
    60, 64, 67, 69,   # Bar 2
    60, 61, 64, 67    # Bar 3
]
for i, note in enumerate(sax_notes):
    start = 1.5 + (i % 4) * 0.375
    duration = 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])
