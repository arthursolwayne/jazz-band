
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.125, 0.375),   # Hihat on &1
    (38, 0.5, 0.375),     # Snare on 2
    (42, 0.625, 0.375),   # Hihat on &2
    (36, 1.0, 0.375),     # Kick on 3
    (42, 1.125, 0.375),   # Hihat on &3
    (38, 1.5, 0.375)      # Snare on 4
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),     # D2 on 1
    (40, 1.875, 0.375),   # Eb2 on &2
    (43, 2.25, 0.375),    # G2 on 3
    (41, 2.625, 0.375),   # Ab2 on &4
    (38, 3.0, 0.375),     # D2 on 1
    (40, 3.375, 0.375),   # Eb2 on &2
    (43, 3.75, 0.375),    # G2 on 3
    (41, 4.125, 0.375),   # Ab2 on &4
    (38, 4.5, 0.375),     # D2 on 1
    (40, 4.875, 0.375),   # Eb2 on &2
    (43, 5.25, 0.375),    # G2 on 3
    (41, 5.625, 0.375)    # Ab2 on &4
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano - Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (65, 1.5, 0.375),     # F
    (69, 1.5, 0.375),     # A
    (67, 1.5, 0.375),     # C
    (72, 1.5, 0.375),     # E
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    (62, 2.25, 0.375),    # Bb
    (67, 2.25, 0.375),    # D
    (65, 2.25, 0.375),    # F
    (69, 2.25, 0.375),    # Ab
    # Bar 4: D7 (D, F#, A, C)
    (62, 3.0, 0.375),     # D
    (67, 3.0, 0.375),     # F#
    (69, 3.0, 0.375),     # A
    (64, 3.0, 0.375)      # C
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Drums - Little Ray (Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.625, 0.375),   # Hihat on &1
    (38, 2.0, 0.375),     # Snare on 2
    (42, 2.125, 0.375),   # Hihat on &2
    (36, 2.5, 0.375),     # Kick on 3
    (42, 2.625, 0.375),   # Hihat on &3
    (38, 3.0, 0.375),     # Snare on 4
    (42, 3.125, 0.375),   # Hihat on &4
    (36, 3.5, 0.375),     # Kick on 1
    (42, 3.625, 0.375),   # Hihat on &1
    (38, 4.0, 0.375),     # Snare on 2
    (42, 4.125, 0.375),   # Hihat on &2
    (36, 4.5, 0.375),     # Kick on 3
    (42, 4.625, 0.375),   # Hihat on &3
    (38, 5.0, 0.375),     # Snare on 4
    (42, 5.125, 0.375)    # Hihat on &4
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Sax - Dante (One short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
sax_notes = [
    (66, 1.5, 0.375),     # G (F7)
    (69, 1.875, 0.375),   # Bb
    (67, 2.25, 0.375),    # C (F7)
    (66, 2.625, 0.375),   # G (F7)
    (66, 3.0, 0.375),     # G (F7)
    (69, 3.375, 0.375),   # Bb
    (67, 3.75, 0.375),    # C (F7)
    (66, 4.125, 0.375),   # G (F7)
    (66, 4.5, 0.375),     # G (F7)
    (69, 4.875, 0.375),   # Bb
    (67, 5.25, 0.375),    # C (F7)
    (66, 5.625, 0.375)    # G (F7)
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
