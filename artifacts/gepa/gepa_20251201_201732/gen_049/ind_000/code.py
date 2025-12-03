
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
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
]
for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.75), (38, 2.0), (43, 2.25),
    (43, 2.5), (45, 2.75), (43, 3.0), (38, 3.25),
    (38, 3.5), (40, 3.75), (38, 4.0), (43, 4.25),
    (43, 4.5), (45, 4.75), (43, 5.0), (38, 5.25)
]
for note_number, time in bass_notes:
    note = pretty_midi.Note(velocity=70, pitch=note_number, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D4-F#4-A4-C#5)
# Bar 3: Bm7 (B3-D4-F#4-A4)
# Bar 4: G7 (G4-B4-D5-F5) resolving to Dmaj7
piano_notes = [
    # Bar 2: Dmaj7
    (62, 1.5), (64, 1.5), (67, 1.5), (69, 1.5),  # D4, F#4, A4, C#5
    # Bar 3: Bm7
    (66, 2.5), (68, 2.5), (71, 2.5), (73, 2.5),  # B3, D4, F#4, A4
    # Bar 4: G7
    (67, 3.5), (69, 3.5), (72, 3.5), (74, 3.5),  # G4, B4, D5, F5
    # Bar 4: C#5 (resolution)
    (72, 5.0)
]
for note_number, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.5)
    piano.notes.append(note)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Same pattern as before but starting at 1.5s
for i, time in enumerate([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]):
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    elif i % 2 == 1:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), E4 (64), D4 (62), F#4 (66)
# Play on beats 1 and 3 of bar 2
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0), (66, 2.25),
    (62, 3.5), (64, 3.75), (62, 4.0), (66, 4.25)
]
for note_number, time in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=time, end=time + 0.25)
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
