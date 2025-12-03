
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
drum_notes = [
    (36, 0.0, 1.0),   # Kick on 1
    (42, 0.25, 0.25), # Hihat on &1
    (36, 0.75, 0.25), # Kick on 3
    (42, 1.0, 0.5),   # Hihat on &3 and 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.5),   # D2 on 1
    (41, 1.75, 0.5),  # F2 on 2 (chromatic approach)
    (38, 2.5, 0.5),   # D2 on 3
    (43, 2.75, 0.5),  # A2 on 4 (fifth)
    
    (37, 3.0, 0.5),   # C2 on 1
    (39, 3.25, 0.5),  # Eb2 on 2 (chromatic approach)
    (37, 3.75, 0.5),  # C2 on 3
    (42, 4.0, 0.5),   # G2 on 4 (fifth)
    
    (38, 4.5, 0.5),   # D2 on 1
    (40, 4.75, 0.5),  # F#2 on 2 (chromatic approach)
    (38, 5.25, 0.5),  # D2 on 3
    (43, 5.5, 0.5),   # A2 on 4 (fifth)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane on piano: Open voicings, different chords each bar, resolve on the last
# Bar 2: Cm7 (C-Eb-G-Bb)
piano_notes = [
    (60, 1.5, 0.5),   # C
    (63, 1.5, 0.5),   # Eb
    (67, 1.5, 0.5),   # G
    (69, 1.5, 0.5),   # Bb
    
    # Bar 3: F7 (F-A-C-E)
    (65, 3.0, 0.5),   # F
    (68, 3.0, 0.5),   # A
    (72, 3.0, 0.5),   # C
    (76, 3.0, 0.5),   # E
    
    # Bar 4: Dm7 (D-F-A-C)
    (62, 4.5, 0.5),   # D
    (64, 4.5, 0.5),   # F
    (69, 4.5, 0.5),   # A
    (72, 4.5, 0.5),   # C
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 (bar_start)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.25))
    # Snare on 2 (bar_start + 0.5)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.5, end=bar_start + 0.75))
    # Kick on 3 (bar_start + 1.0)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.0, end=bar_start + 1.25))
    # Snare on 4 (bar_start + 1.5)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.75))
    # Hihat on every eighth
    for i in range(0, 6):
        hihat_start = bar_start + i * 0.25
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125))

# Dante on sax: One short motif, haunting, incomplete
# Bar 2: Start the motif
sax_notes = [
    (62, 1.5, 0.5),   # D (start of motif)
    (65, 1.75, 0.25), # F (flicker)
    (62, 2.0, 0.25),  # D (rest)
    # Bar 3: Continue the motif with space
    (67, 3.0, 0.25),  # G (answer)
    (64, 3.25, 0.25), # F (shadow)
    (62, 3.75, 0.25), # D (return)
    # Bar 4: End the motif, leave it hanging
    (67, 4.5, 0.5),   # G (final note)
    (64, 4.75, 0.25), # F (leave it unresolved)
    (62, 5.0, 0.25),  # D (space)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
