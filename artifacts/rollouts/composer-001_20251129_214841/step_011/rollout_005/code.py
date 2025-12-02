
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
midi.tempo_changes = [pretty_midi.TempoChange(120, 0.0)]

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
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=i * 0.375, end=(i + 1) * 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=(i + 1) * 0.375, end=(i + 2) * 0.375)
    drums.notes.append(kick)
    drums.notes.append(snare)

for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=hihat_notes[i], start=i * 0.1875, end=(i + 1) * 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    62, 63, 64, 65,  # Bar 2
    65, 64, 63, 62,  # Bar 3
    62, 63, 64, 65   # Bar 4
]
for i, note in enumerate(bass_notes):
    start = 1.5 + (i % 4) * 0.375
    end = start + 0.375
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    64, 67, 71, 72,  # C7
    # Bar 3
    64, 67, 71, 76,  # F7
    # Bar 4
    64, 67, 71, 72   # C7
]
for i, note in enumerate(piano_notes):
    start = 1.5 + (i // 4) * 1.5 + ((i % 4) + 1) * 0.375
    end = start + 0.375
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    67, 69, 71, 72,  # C E G B
    # Bar 3
    72, 69, 67, 64,  # B E C C
    # Bar 4
    67, 69, 71, 72   # C E G B
]
for i, note in enumerate(sax_notes):
    start = 1.5 + (i // 4) * 1.5 + ((i % 4)) * 0.375
    end = start + 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    sax.notes.append(sax_note)

# Drums: continue with same pattern
for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i * 0.375, end=1.5 + (i + 1) * 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=1.5 + (i + 1) * 0.375, end=1.5 + (i + 2) * 0.375)
    drums.notes.append(kick)
    drums.notes.append(snare)

for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i * 0.1875, end=1.5 + (i + 1) * 0.1875)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
