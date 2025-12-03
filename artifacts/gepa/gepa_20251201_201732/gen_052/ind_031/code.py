
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

# Drums: Bar 1
drum_notes = [
    (36, 0.0, 1.0),     # Kick on 1
    (42, 0.375, 0.75),  # Hihat on &1
    (38, 0.75, 1.0),    # Snare on 2
    (42, 1.125, 1.5),   # Hihat on &3
    (36, 1.5, 1.75),    # Kick on 3
    (42, 1.875, 2.25),  # Hihat on &3
    (38, 2.25, 2.5),    # Snare on 4
    (42, 2.625, 3.0),   # Hihat on &4
]

for note, start, end in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 1.75),    # D2 on 1
    (40, 1.75, 2.0),    # Eb2 chromatic approach on &2
    (43, 2.0, 2.25),    # G2 on 2
    (41, 2.25, 2.5),    # F2 chromatic approach on &3
    (38, 2.5, 2.75),    # D2 on 3
    (40, 2.75, 3.0),    # Eb2 chromatic approach on &4
]

for note, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    (62, 1.5, 1.75),    # D4
    (67, 1.5, 1.75),    # F#4
    (69, 1.5, 1.75),    # A4
    (64, 1.5, 1.75),    # C4
]

for note, start, end in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging.
sax_notes = [
    (67, 1.75, 2.0),    # F4 on &2
    (69, 2.0, 2.25),    # A4 on 2
    (67, 2.25, 2.5),    # F4 on &3 (rest on 3)
]

for note, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(note)

# Bar 3: (3.0 - 4.5s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (43, 3.0, 3.25),    # G2 on 1
    (45, 3.25, 3.5),    # A2 chromatic approach on &2
    (38, 3.5, 3.75),    # D2 on 2
    (40, 3.75, 4.0),    # Eb2 chromatic approach on &3
    (43, 4.0, 4.25),    # G2 on 3
    (45, 4.25, 4.5),    # A2 chromatic approach on &4
]

for note, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(note)

# Piano: Bar 3: Bm7b5 (B D F A)
piano_notes = [
    (71, 3.0, 3.25),    # B4
    (67, 3.0, 3.25),    # F#4 (not in chord — tension)
    (69, 3.0, 3.25),    # A4
    (64, 3.0, 3.25),    # C4 (not in chord — tension)
    (62, 3.25, 3.5),    # D4 on &2
    (64, 3.5, 3.75),    # C4 on 2
    (67, 3.75, 4.0),    # F#4 on &3
    (69, 4.0, 4.25),    # A4 on 3
    (62, 4.25, 4.5),    # D4 on &4
]

for note, start, end in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(note)

# Sax: Haunting but incomplete. Rest on 1 and 3, play on 2 and 4
sax_notes = [
    (69, 3.25, 3.5),    # A4 on &2
    (67, 3.5, 3.75),    # F4 on 2
    (69, 4.25, 4.5),    # A4 on &4
]

for note, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(note)

# Bar 4: (4.5 - 6.0s)

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 4.75),    # Kick on 1
    (42, 4.875, 5.25),  # Hihat on &1
    (38, 5.25, 5.5),    # Snare on 2
    (42, 5.625, 6.0),   # Hihat on &3
    (36, 5.75, 6.0),    # Kick on 3 (slightly late for tension)
    (38, 6.0, 6.25),    # Snare on 4 (outside of bar, for tension)
]

for note, start, end in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    drums.notes.append(dr)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 4.5, 4.75),    # D2 on 1
    (40, 4.75, 5.0),    # Eb2 chromatic approach on &2
    (43, 5.0, 5.25),    # G2 on 2
    (41, 5.25, 5.5),    # F2 chromatic approach on &3
    (38, 5.5, 5.75),    # D2 on 3
    (40, 5.75, 6.0),    # Eb2 chromatic approach on &4
]

for note, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(note)

# Piano: Bar 4: G7 (G B D F)
piano_notes = [
    (67, 4.5, 4.75),    # G4
    (71, 4.5, 4.75),    # B4
    (69, 4.5, 4.75),    # A4 (not in chord — tension)
    (64, 4.5, 4.75),    # C4 (not in chord — tension)
    (67, 4.75, 5.0),    # G4 on &2
    (69, 5.0, 5.25),    # A4 on 2
    (64, 5.25, 5.5),    # C4 on &3
    (67, 5.5, 5.75),    # G4 on 3
    (69, 5.75, 6.0),    # A4 on &4
]

for note, start, end in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(note)

# Sax: Return to the motif, finish it. Rest on 1 and 3, play on 2 and 4
sax_notes = [
    (67, 4.75, 5.0),    # F4 on &2
    (69, 5.0, 5.25),    # A4 on 2
    (67, 5.25, 5.5),    # F4 on &3 (rest on 3)
    (69, 5.75, 6.0),    # A4 on &4
]

for note, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
