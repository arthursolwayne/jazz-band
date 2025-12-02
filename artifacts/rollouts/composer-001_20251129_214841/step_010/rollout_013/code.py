
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i in range(2):
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=bar1_start + i * 0.75, end=bar1_start + i * 0.75 + 0.375)
    drums.notes.append(kick)
    snare = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=bar1_start + i * 0.75 + 0.375, end=bar1_start + i * 0.75 + 0.75)
    drums.notes.append(snare)
for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=hihat_notes[i], start=bar1_start + i * 0.1875, end=bar1_start + i * 0.1875 + 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif - start with a short phrase
sax_notes = [
    (62, 1.5, 1.75),  # D5
    (64, 1.75, 2.0),  # E5
    (60, 2.0, 2.25),  # C5
    (62, 2.25, 2.5),  # D5
    (64, 2.5, 2.75),  # E5
    (62, 2.75, 3.0),  # D5
    (60, 3.0, 3.25),  # C5
    (62, 3.25, 3.5),  # D5
    (64, 3.5, 3.75),  # E5
    (62, 3.75, 4.0),  # D5
    (60, 4.0, 4.25),  # C5
    (62, 4.25, 4.5),  # D5
    (64, 4.5, 4.75),  # E5
    (62, 4.75, 5.0),  # D5
    (60, 5.0, 5.25),  # C5
    (62, 5.25, 5.5),  # D5
    (64, 5.5, 5.75),  # E5
    (62, 5.75, 6.0)   # D5
]

for note in sax_notes:
    pitch, start, end = note
    sax_note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(sax_note)

# Bass line - walking line with chromatic approaches
bass_notes = [
    (60, 1.5, 1.75),  # C4
    (61, 1.75, 2.0),  # C#4
    (62, 2.0, 2.25),  # D4
    (63, 2.25, 2.5),  # D#4
    (64, 2.5, 2.75),  # E4
    (65, 2.75, 3.0),  # F4
    (66, 3.0, 3.25),  # F#4
    (67, 3.25, 3.5),  # G4
    (68, 3.5, 3.75),  # G#4
    (69, 3.75, 4.0),  # A4
    (70, 4.0, 4.25),  # A#4
    (71, 4.25, 4.5),  # B4
    (72, 4.5, 4.75),  # C5
    (71, 4.75, 5.0),  # B4
    (70, 5.0, 5.25),  # A#4
    (69, 5.25, 5.5),  # A4
    (68, 5.5, 5.75),  # G#4
    (67, 5.75, 6.0)   # G4
]

for note in bass_notes:
    pitch, start, end = note
    bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(bass_note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    (72, 1.75, 2.0),  # C5 (root)
    (74, 1.75, 2.0),  # E5 (major third)
    (76, 1.75, 2.0),  # G5 (fifth)
    (79, 1.75, 2.0),  # Bb5 (minor seventh)
    (72, 3.25, 3.5),  # C5
    (74, 3.25, 3.5),  # E5
    (76, 3.25, 3.5),  # G5
    (79, 3.25, 3.5),  # Bb5
    (72, 4.75, 5.0),  # C5
    (74, 4.75, 5.0),  # E5
    (76, 4.75, 5.0),  # G5
    (79, 4.75, 5.0)   # Bb5
]

for note in piano_notes:
    pitch, start, end = note
    piano_note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    piano.notes.append(piano_note)

# Drums for bars 2-4
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

for bar_start in [bar2_start, bar3_start, bar4_start]:
    for i in range(2):
        kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + i * 0.75, end=bar_start + i * 0.75 + 0.375)
        drums.notes.append(kick)
        snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + i * 0.75 + 0.375, end=bar_start + i * 0.75 + 0.75)
        drums.notes.append(snare)
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.1875, end=bar_start + i * 0.1875 + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
