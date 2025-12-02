
import pretty_midi

# Initialize the PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
drums_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
sax_program = pretty_midi.instrument_name_to_program("Tenor Saxophone")
piano_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
bass_program = pretty_midi.instrument_name_to_program("Double Bass")

drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)
piano = pretty_midi.Instrument(program=piano_program)
bass = pretty_midi.Instrument(program=bass_program)

pm.instruments = [drums, sax, piano, bass]

# Time per bar = 1.5 seconds (160 BPM)
bar_length = 1.5
note_length = 0.375  # 1/4 note

# ---------------------------
# 🥁 DRUMS: Bar 1
# ---------------------------

# Bar 1: Hihat on every 8th, kick on 1 and 3, snare on 2 and 4
for i in range(8):
    note_time = i * note_length
    # Hihat
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=note_time, end=note_time + note_length / 2)
    drums.notes.append(hihat)

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0, end=note_length))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=note_length * 2, end=note_length * 3))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=note_length, end=note_length * 2))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=note_length * 3, end=note_length * 4))

# ---------------------------
# 🎶 SAX: Bar 4
# ---------------------------

# Simple, emotive motif: D - F# - B - D
# Time: 0.0 to 1.5 seconds
# Note values: quarter, eighth, eighth, quarter (dotted)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=0.0, end=0.375),     # D4
    pretty_midi.Note(velocity=100, pitch=67, start=0.375, end=0.75),    # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=0.75, end=1.125),    # B4
    pretty_midi.Note(velocity=100, pitch=62, start=1.125, end=1.5),     # D4
]
sax.notes.extend(sax_notes)

# ---------------------------
# 🎹 PIANO: Bars 2-4
# ---------------------------

# Bar 2: Comp on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875))  # F#4

# Bar 3: Comp on beat 2 (7th chords)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375))  # F#4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375))  # B4

# Bar 4: Comp on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875))  # F#4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875))  # B4

# ---------------------------
# 🎻 BASS: Bars 2-4
# ---------------------------

# Walking bass line in D major: D - C - B - A - G - F# - E - D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),   # D4
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # C4
    pretty_midi.Note(velocity=80, pitch=61, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=80, pitch=59, start=2.625, end=3.0),   # A4
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),   # G4
    pretty_midi.Note(velocity=80, pitch=56, start=3.375, end=3.75),  # F#4
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),   # D4
]
bass.notes.extend(bass_notes)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
