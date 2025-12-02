
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(120, 0)]

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
hihat_notes = [42, 42, 42, 42, 42, 42, 42, 42]

for i in range(4):
    kick_time = i * 0.375
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=kick_time, end=kick_time + 0.125)
    drums.notes.append(kick)

for i in range(4):
    snare_time = (i + 1) * 0.375
    snare = pretty_midi.Note(velocity=110, pitch=snare_notes[i], start=snare_time, end=snare_time + 0.125)
    drums.notes.append(snare)

for i in range(8):
    hihat_time = i * 0.1875
    hihat = pretty_midi.Note(velocity=80, pitch=hihat_notes[i], start=hihat_time, end=hihat_time + 0.125)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in C
bass_notes = [
    60, 62, 63, 64,  # Bar 2
    65, 67, 69, 71,  # Bar 3
    72, 71, 69, 67   # Bar 4
]
for i, note in enumerate(bass_notes):
    start_time = 1.5 + i * 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=start_time + 0.25)
    bass.notes.append(bass_note)

# Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    60, 64, 67, 71,  # C7
    # Bar 3: D7 on beat 2
    62, 67, 71, 76,  # D7
    # Bar 4: E7 on beat 2
    64, 69, 74, 79   # E7
]
for i, chord in enumerate(piano_notes):
    start_time = 1.5 + (i // 4) * 1.5 + (i % 4) * 0.375
    if start_time >= 1.5 and start_time < 6.0:
        piano_note = pretty_midi.Note(velocity=90, pitch=chord, start=start_time, end=start_time + 0.125)
        piano.notes.append(piano_note)

# Dante - Tenor sax motif (start, leave hanging, finish)
sax_notes = [
    # Bar 2: Start of motif (C, E, G)
    60, 64, 67, 64,  # C E G E
    # Leave it hanging (rest)
    # Bar 3: Continue (D, F, A)
    62, 65, 69, 65,  # D F A F
    # Bar 4: Finish (E, G, B)
    64, 67, 71, 67   # E G B G
]
for i, note in enumerate(sax_notes):
    start_time = 1.5 + (i // 4) * 1.5 + (i % 4) * 0.375
    if start_time >= 1.5 and start_time < 6.0:
        sax_note = pretty_midi.Note(velocity=105, pitch=note, start=start_time, end=start_time + 0.25)
        sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
