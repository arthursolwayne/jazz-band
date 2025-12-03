
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# D: D2 (38), A2 (43), chromatic approach to D2 (37), then A2 (43), chromatic G#2 (42)
bass_notes = [
    (37, 1.5, 0.375), # chromatic approach to D2
    (38, 1.5, 0.375), # D2
    (42, 1.875, 0.375), # chromatic approach to A2
    (43, 1.875, 0.375), # A2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#) - open voicings
piano_notes = [
    (50, 1.5, 0.375), # D
    (53, 1.5, 0.375), # F#
    (57, 1.5, 0.375), # A
    (61, 1.5, 0.375), # C#
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante: Sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (65), G (67) - fragment, hanging on F#
sax_notes = [
    (62, 1.5, 0.375), # D
    (65, 1.875, 0.375), # F#
    (67, 2.25, 0.375), # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# D: D2 (38), A2 (43), chromatic approach to D2 (37), then A2 (43), chromatic G#2 (42)
bass_notes = [
    (37, 3.0, 0.375), # chromatic approach to D2
    (38, 3.0, 0.375), # D2
    (42, 3.375, 0.375), # chromatic approach to A2
    (43, 3.375, 0.375), # A2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G, B, D, F#) - open voicings
piano_notes = [
    (55, 3.0, 0.375), # G
    (58, 3.0, 0.375), # B
    (62, 3.0, 0.375), # D
    (66, 3.0, 0.375), # F#
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante: Sax - continue motif, finish it
# F# (65), G (67), A (69) - resolved motif
sax_notes = [
    (65, 3.0, 0.375), # F#
    (67, 3.375, 0.375), # G
    (69, 3.75, 0.375), # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# D: D2 (38), A2 (43), chromatic approach to D2 (37), then A2 (43), chromatic G#2 (42)
bass_notes = [
    (37, 4.5, 0.375), # chromatic approach to D2
    (38, 4.5, 0.375), # D2
    (42, 4.875, 0.375), # chromatic approach to A2
    (43, 4.875, 0.375), # A2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C, E, G, B) - open voicings
piano_notes = [
    (52, 4.5, 0.375), # C
    (55, 4.5, 0.375), # E
    (59, 4.5, 0.375), # G
    (63, 4.5, 0.375), # B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante: Sax - end the motif
# A (69), G (67), F# (65) - resolution
sax_notes = [
    (69, 4.5, 0.375), # A
    (67, 4.875, 0.375), # G
    (65, 5.25, 0.375), # F#
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick=36, snare=38, hihat=42
# Bar 4: Full rhythm, fill the bar
drum_notes = [
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
