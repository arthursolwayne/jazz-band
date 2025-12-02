
import pretty_midi
from pretty_midi import Note, Instrument

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI()

# Set tempo to 160 BPM
pm.time_signature_changes = []
pm.time_signature_changes.append(pretty_midi.TimeSignature(4, 4, 0.0))

# Set tempo to 160 BPM
pm.tempo_changes = []
pm.tempo_changes.append(pretty_midi.TempoChange(160.0, 0.0))

# Define the key: F minor (F, Gb, Ab, Bb, Bb, Db, Eb)
# We'll use F minor (F, Gb, Ab, Bb, Bb, Db, Eb)

# Bar 1: Little Ray on drums
drum_program = pretty_midi.instrument_name_to_program("Drums")
drum_inst = Instrument(program=drum_program, is_drum=True)

# Kick on 1 and 3
kick_notes = [Note(36, 1.0, 0.0), Note(36, 1.0, 1.5)]
drum_inst.notes.extend(kick_notes)

# Snare on 2 and 4
snare_notes = [Note(38, 1.0, 0.75), Note(38, 1.0, 2.25)]
drum_inst.notes.extend(snare_notes)

# Hi-hat on every eighth
hihat_notes = []
for i in range(0, 6, 0.375):
    hihat_notes.append(Note(42, 0.1, i))
drum_inst.notes.extend(hihat_notes)

pm.instruments.append(drum_inst)

# Bar 2-4: Quartet in

# Bass (Marcus) – walking line, chromatic approaches
bass_program = pretty_midi.instrument_name_to_program("Acoustic Bass")
bass_inst = Instrument(program=bass_program)

# Fm key: F, Gb, Ab, Bb, Bb, Db, Eb

# Walking line: F, Gb, Ab, Bb (bar 2)
bass_notes = [
    Note(64, 1.0, 1.5),  # F
    Note(65, 1.0, 1.875),  # Gb
    Note(66, 1.0, 2.25),  # Ab
    Note(67, 1.0, 2.625),  # Bb
    Note(67, 1.0, 2.875),  # Bb
    Note(69, 1.0, 3.25),  # Db
    Note(70, 1.0, 3.625),  # Eb
    Note(64, 1.0, 3.875),  # F
]

bass_inst.notes.extend(bass_notes)
pm.instruments.append(bass_inst)

# Piano (Diane) – 7th chords, comp on 2 and 4
piano_program = pretty_midi.instrument_name_to_program("Acoustic Piano")
piano_inst = Instrument(program=piano_program)

# F7 chord: F, Ab, Bb, C (but we're in Fm, so maybe F7 with altered)
# F7 (F, A, C, Eb) – but we're in Fm, so maybe F7#9 or F7b9?

# Comp on 2 and 4 of bar 2
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, Eb)
    Note(64, 1.0, 1.875),  # F
    Note(67, 1.0, 1.875),  # A
    Note(69, 1.0, 1.875),  # C
    Note(71, 1.0, 1.875),  # Eb

    # Bar 2, beat 4: F7 again
    Note(64, 1.0, 2.625),  # F
    Note(67, 1.0, 2.625),  # A
    Note(69, 1.0, 2.625),  # C
    Note(71, 1.0, 2.625),  # Eb

    # Bar 3, beat 2: Bb7 (Bb, D, F, Ab)
    Note(67, 1.0, 3.375),  # Bb
    Note(70, 1.0, 3.375),  # D
    Note(64, 1.0, 3.375),  # F
    Note(66, 1.0, 3.375),  # Ab

    # Bar 3, beat 4: Ab7 (Ab, C, Eb, Gb)
    Note(66, 1.0, 4.125),  # Ab
    Note(69, 1.0, 4.125),  # C
    Note(71, 1.0, 4.125),  # Eb
    Note(65, 1.0, 4.125),  # Gb
]

piano_inst.notes.extend(piano_notes)
pm.instruments.append(piano_inst)

# Tenor Sax (You) – sparse, expressive motif
tenor_program = pretty_midi.instrument_name_to_program("Tenor Saxophone")
tenor_inst = Instrument(program=tenor_program)

# Start of bar 2: Motif begins
# F, Ab, Bb, then a rest in bar 3, then F again on beat 3 of bar 4
# Make it feel like a memory trying to return – sparse but filled with space

# Bar 2
tenor_notes = [
    Note(64, 1.0, 1.5),  # F
    Note(66, 1.0, 1.875),  # Ab
    Note(67, 1.0, 2.25),  # Bb
]

# Bar 3 – remainder is space
# Bar 4 – return
tenor_notes.append(Note(64, 1.0, 3.75))  # F on beat 3 of bar 4

tenor_inst.notes.extend(tenor_notes)
pm.instruments.append(tenor_inst)

# Save the MIDI file
pm.write("jazz_intro_in_fm.mid")
