
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature (4/4)
pm.time_signature_changes[0].numerator = 4
pm.time_signature_changes[0].denominator = 4

# Define key: D major
pm.key_signature_changes[0].key_number = 2  # D major

# Instrument tracks
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Drum kit is on channel 9
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program, is_drum=True)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time per bar in seconds (160 BPM = 60/160 = 0.375 seconds per beat, 1.5 seconds per bar)
bar_length = 1.5

# --- BASS LINE: Marcus (Walking line, D2-G2, roots and fifths with chromatic approaches)
# Bar 1: Rest
# Bar 2: Root (D2), chromatic approach (D#2), then root (D2)
# Bar 3: Root (D2), chromatic (D#2), then fifth (A2)
# Bar 4: Root (D2), chromatic (D#2), then root (D2)

# Bar 2
note = pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.5 + 0.375)  # D2
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=63, start=1.5 + 0.375, end=1.5 + 0.75)  # D#2
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 0.75, end=1.5 + 1.5)  # D2
bass.notes.append(note)

# Bar 3
note = pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 1.5, end=1.5 + 1.875)  # D2
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=63, start=1.5 + 1.875, end=1.5 + 2.25)  # D#2
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=1.5 + 2.25, end=1.5 + 3.0)  # A2
bass.notes.append(note)

# Bar 4
note = pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 3.0, end=1.5 + 3.375)  # D2
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=63, start=1.5 + 3.375, end=1.5 + 3.75)  # D#2
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 3.75, end=1.5 + 4.5)  # D2
bass.notes.append(note)

# --- PIANO: Diane (Open voicings, resolve on the last beat of each bar)
# Bar 1: Rest
# Bar 2: C (Dm7) -> D (G7) -> E (Cmaj7)
# Bar 3: C (Dm7) -> D (G7) -> E (Cmaj7)
# Bar 4: C (Dm7) -> D (G7) -> E (Cmaj7)

# Bar 2
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.375)  # C4 (Dm7)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 0.375, end=1.5 + 0.75)  # D4 (G7)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 0.75, end=1.5 + 1.5)  # E4 (Cmaj7)
piano.notes.append(note)

# Bar 3
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 1.5, end=1.5 + 1.875)  # C4 (Dm7)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 1.875, end=1.5 + 2.25)  # D4 (G7)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 2.25, end=1.5 + 3.0)  # E4 (Cmaj7)
piano.notes.append(note)

# Bar 4
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 3.0, end=1.5 + 3.375)  # C4 (Dm7)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 3.375, end=1.5 + 3.75)  # D4 (G7)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 3.75, end=1.5 + 4.5)  # E4 (Cmaj7)
piano.notes.append(note)

# --- DRUMS: Little Ray (Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth)
# Bar 1: Kick on 1, snare on 2, hi-hat on 3, kick on 4
# Bar 2: Kick on 1, snare on 2, hi-hat on 3, kick on 4
# Bar 3: Kick on 1, snare on 2, hi-hat on 3, kick on 4
# Bar 4: Kick on 1, snare on 2, hi-hat on 3, kick on 4

# Kick (C1, MIDI 36)
# Snare (Snare Drum, MIDI 38)
# Hi-hat (Closed Hi-hat, MIDI 42)

# Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + 0.375),      # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.375 + 0.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.75 + 0.375),    # Hi-hat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.125 + 0.375)  # Kick on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.5 + 0.375),      # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + 0.375, end=1.5 + 0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + 0.75, end=1.5 + 1.125),    # Hi-hat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + 1.125, end=1.5 + 1.5)  # Kick on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + 1.5, end=1.5 + 1.875),      # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + 1.875, end=1.5 + 2.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + 2.25, end=1.5 + 2.625),    # Hi-hat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + 2.625, end=1.5 + 3.0)  # Kick on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + 3.0, end=1.5 + 3.375),      # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + 3.375, end=1.5 + 3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + 3.75, end=1.5 + 4.125),    # Hi-hat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + 4.125, end=1.5 + 4.5)  # Kick on 4
]
for note in drum_notes:
    drums.notes.append(note)

# --- SAX: Dante (Tenor, short motif, make it sing. Start strong, leave it hanging, come back to finish)
# Bar 1: Little Ray alone
# Bar 2: Start of motif (A4, G4, B4)
# Bar 3: Rest
# Bar 4: End of motif (A4)

# Bar 2
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.375)  # A4
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.375, end=1.5 + 0.75)  # G4
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 0.75, end=1.5 + 1.125)  # B4
sax.notes.append(note)

# Bar 4
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 3.0, end=1.5 + 4.5)  # A4 (ends on the last beat of the final bar)
sax.notes.append(note)

# Save the MIDI
pm.write('dante_intro.mid')
print("MIDI file 'dante_intro.mid' has been created.")
