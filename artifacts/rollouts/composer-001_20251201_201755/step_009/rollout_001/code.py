
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [bar1_start + 0.0, bar1_start + 0.75]
snare_times = [bar1_start + 0.375, bar1_start + 1.125]
hihat_times = [bar1_start + t * 0.375 for t in range(0, 4)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Marcus on bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, bar2_start, bar2_start + 0.25),     # D2
    (40, bar2_start + 0.25, bar2_start + 0.5), # F2 (chromatic approach)
    (43, bar2_start + 0.5, bar2_start + 0.75), # G2
    (40, bar2_start + 0.75, bar2_start + 1.0), # F2
    (38, bar2_start + 1.0, bar2_start + 1.25), # D2
    (40, bar2_start + 1.25, bar2_start + 1.5), # F2 (chromatic approach)
    (43, bar2_start + 1.5, bar2_start + 1.75), # G2
    (40, bar2_start + 1.75, bar2_start + 2.0)  # F2
]
for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
chord2 = [62, 66, 69, 72]
for pitch in chord2:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar2_start, end=bar2_end)
    piano.notes.append(note)

# Bar 3: G7 (G B D F)
chord3 = [67, 71, 74, 76]
for pitch in chord3:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar2_end, end=bar2_end + 1.5)
    piano.notes.append(note)

# Bar 4: C7 (C E G B)
chord4 = [60, 64, 67, 71]
for pitch in chord4:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar2_end + 1.5, end=bar2_end + 3.0)
    piano.notes.append(note)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (66), G (67), D (62) - play first two notes, leave the rest hanging
sax_notes = [
    (62, bar2_start, bar2_start + 0.375),    # D
    (66, bar2_start + 0.375, bar2_start + 0.75), # F#
    (67, bar2_start + 0.75, bar2_start + 1.125), # G
    (62, bar2_start + 1.125, bar2_start + 1.5)   # D
]
for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [bar2_start, bar2_start + 1.5, bar2_start + 3.0]:
    kick_times = [bar + 0.0, bar + 0.75]
    snare_times = [bar + 0.375, bar + 1.125]
    hihat_times = [bar + t * 0.375 for t in range(0, 4)]
    
    for t in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
        drums.notes.append(note)
    
    for t in snare_times:
        note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
        drums.notes.append(note)

    for t in hihat_times:
        note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.1)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
