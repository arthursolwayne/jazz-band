
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36]
snare_notes = [38]
hihat_notes = [42]

# Kick on 1 and 3
kick_times = [bar1_start + 0.0, bar1_start + 0.75]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [bar1_start + 0.375, bar1_start + 1.125]
for time in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

# Hihat on every eighth
hihat_times = [bar1_start + 0.0, bar1_start + 0.375, bar1_start + 0.75, bar1_start + 1.125]
for time in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5),      # D2
    (40, 1.875),    # F2
    (43, 2.25),     # G2
    (41, 2.625),    # F#2
    (38, 3.0),      # D2
    (40, 3.375),    # F2
    (43, 3.75),     # G2
    (41, 4.125),    # F#2
    (38, 4.5),      # D2
    (40, 4.875),    # F2
    (43, 5.25),     # G2
    (41, 5.625)     # F#2
]

for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
bar2_start = 1.5
bar2_end = 3.0
bar3_start = 3.0
bar3_end = 4.5
bar4_start = 4.5
bar4_end = 6.0

# Bar 2: Dm7 (D, F, A, C)
piano_notes_bar2 = [
    (62, bar2_start),   # D4
    (65, bar2_start),   # F4
    (69, bar2_start),   # A4
    (71, bar2_start),   # C5
]
for pitch, time in piano_notes_bar2:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=bar2_end)
    piano.notes.append(note)

# Bar 3: G7 (G, B, D, F)
piano_notes_bar3 = [
    (67, bar3_start),   # G4
    (71, bar3_start),   # B4
    (69, bar3_start),   # D5
    (65, bar3_start),   # F5
]
for pitch, time in piano_notes_bar3:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=bar3_end)
    piano.notes.append(note)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes_bar4 = [
    (60, bar4_start),   # C4
    (63, bar4_start),   # Eb4
    (67, bar4_start),   # G4
    (62, bar4_start),   # Bb4
]
for pitch, time in piano_notes_bar4:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=bar4_end)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, G, A, Bb (D4, G4, A4, Bb4)

sax_notes = [
    (62, 1.5),    # D4
    (67, 1.875),  # G4
    (69, 2.25),   # A4
    (62, 2.625),  # Bb4 (but instead play Bb4 at 2.625, leave it hanging)
    (62, 4.5),    # D4 again, finish the motif
    (67, 4.875),  # G4
    (69, 5.25),   # A4
    (62, 5.625)   # Bb4
]

for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
