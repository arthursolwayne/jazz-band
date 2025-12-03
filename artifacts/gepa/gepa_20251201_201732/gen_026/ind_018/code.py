
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
bar1_start = 0.0
bar1_end = 1.5
for beat in [0, 2]:
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + beat * 0.375, end=bar1_start + beat * 0.375 + 0.1)
    drums.notes.append(kick)
for beat in [1, 3]:
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + beat * 0.375, end=bar1_start + beat * 0.375 + 0.1)
    drums.notes.append(snare)
for beat in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + beat * 0.125, end=bar1_start + beat * 0.125 + 0.05)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line starting at F2 (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5),    # F2
    (40, 1.75),   # Ab2 (chromatic approach)
    (43, 2.0),    # C3 (F root on beat 3)
    (45, 2.25),   # D3 (chromatic approach)
    (38, 2.5),    # F2
    (40, 2.75),   # Ab2
    (43, 3.0),    # C3
    (45, 3.25),   # D3
    (38, 3.5),    # F2
    (40, 3.75),   # Ab2
    (43, 4.0),    # C3
    (45, 4.25),   # D3
    (38, 4.5),    # F2
    (40, 4.75),   # Ab2
    (43, 5.0),    # C3
    (45, 5.25)    # D3
]
for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (65, 1.5), (69, 1.5), (72, 1.5), (76, 1.5),
    (65, 1.75), (69, 1.75), (72, 1.75), (76, 1.75),
    (65, 2.0), (69, 2.0), (72, 2.0), (76, 2.0),
    (65, 2.25), (69, 2.25), (72, 2.25), (76, 2.25),
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    (61, 2.5), (65, 2.5), (68, 2.5), (71, 2.5),
    (61, 2.75), (65, 2.75), (68, 2.75), (71, 2.75),
    (61, 3.0), (65, 3.0), (68, 3.0), (71, 3.0),
    (61, 3.25), (65, 3.25), (68, 3.25), (71, 3.25),
    # Bar 4: Dm7 (D, F, A, C)
    (62, 3.5), (66, 3.5), (69, 3.5), (72, 3.5),
    (62, 3.75), (66, 3.75), (69, 3.75), (72, 3.75),
    (62, 4.0), (66, 4.0), (69, 4.0), (72, 4.0),
    (62, 4.25), (66, 4.25), (69, 4.25), (72, 4.25)
]
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - Bb - F
sax_notes = [
    (72, 1.5, 0.5),  # F
    (74, 2.0, 0.5),  # G
    (71, 2.5, 0.5),  # Bb
    (72, 3.0, 0.5)   # F
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Drums in bars 2-4
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_bar_drums(start):
    for beat in [0, 2]:
        kick = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(kick)
    for beat in [1, 3]:
        snare = pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(snare)
    for beat in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + beat * 0.125, end=start + beat * 0.125 + 0.05)
        drums.notes.append(hihat)

add_bar_drums(bar2_start)
add_bar_drums(bar3_start)
add_bar_drums(bar4_start)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('jazz_intro.mid')
