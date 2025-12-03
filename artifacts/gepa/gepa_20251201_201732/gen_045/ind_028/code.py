
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum notes
kick = 36  # Kick drum
snare = 38  # Snare drum
hihat = 42  # Hi-hat

# Bar 1: Only drums (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    (kick, 0.0), (hihat, 0.375), (hihat, 0.75), (snare, 1.0),
    (hihat, 1.125), (hihat, 1.5), (kick, 1.5)
]

for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Root and fifth with chromatic approach
# F (F3), C (C4), chromatic approach to Bb (Bb4)
bass_notes = [
    (pretty_midi.Note(velocity=70, pitch=71, start=1.5, end=1.75)),  # F3
    (pretty_midi.Note(velocity=70, pitch=76, start=1.75, end=2.0)),  # C4
    (pretty_midi.Note(velocity=70, pitch=75, start=2.0, end=2.25)),  # Bb4 (chromatic approach)
    (pretty_midi.Note(velocity=70, pitch=76, start=2.25, end=2.5)),  # C4
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, each bar has a different chord, resolve on last
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bar 2: Fmaj7
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # A3
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.75),  # C4
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.75),  # E4

    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=70, start=2.0, end=2.25),  # Bb3
    pretty_midi.Note(velocity=100, pitch=75, start=2.0, end=2.25),  # D3
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),  # F3
    pretty_midi.Note(velocity=100, pitch=78, start=2.0, end=2.25),  # Ab3

    # Bar 4: Cm7
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),  # C3
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75),  # Eb3
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=2.75),  # G3
    pretty_midi.Note(velocity=100, pitch=82, start=2.5, end=2.75),  # Bb3
]

piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing
# Start with a short phrase in F: F - Bb - F
# Rest on the 2nd beat, then resolve on the 4th
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=110, pitch=75, start=1.75, end=2.0),  # Bb3
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),  # F3 (resolve)
]

sax.notes.extend(sax_notes)

# Add the remaining drum pattern
# Bar 3: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    (kick, 2.0), (hihat, 2.375), (hihat, 2.75), (snare, 3.0),
    (hihat, 3.125), (hihat, 3.5), (kick, 3.5)
]

for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bar 4: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    (kick, 3.0), (hihat, 3.375), (hihat, 3.75), (snare, 4.0),
    (hihat, 4.125), (hihat, 4.5), (kick, 4.5)
]

for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
print("MIDI file written to 'dante_intro.mid'")
