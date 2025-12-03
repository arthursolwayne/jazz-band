
import pretty_midi
from pretty_midi import Note, Instrument

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Dm key: D, F, A
# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Function to convert beats to seconds (1 beat = 0.375s at 160 BPM)
def beat_to_sec(beats):
    return beats * (60.0 / 160.0)

# Bar 1: Drums only
def create_drums():
    drum_program = 0  # Acoustic Drum Kit
    drum_inst = Instrument(program=drum_program)
    pm.instruments.append(drum_inst)

    # Kick on 1 and 3
    kick_notes = [
        Note(36, 0, beat_to_sec(0), beat_to_sec(0) + 0.05),
        Note(36, 0, beat_to_sec(2), beat_to_sec(2) + 0.05),
    ]
    for note in kick_notes:
        drum_inst.notes.append(note)

    # Snare on 2 and 4
    snare_notes = [
        Note(38, 0, beat_to_sec(1), beat_to_sec(1) + 0.05),
        Note(38, 0, beat_to_sec(3), beat_to_sec(3) + 0.05),
    ]
    for note in snare_notes:
        drum_inst.notes.append(note)

    # Hi-hats on every eighth note
    for i in range(8):
        time = beat_to_sec(i * 0.5)
        hihat = Note(42, 0, time, time + 0.01)
        drum_inst.notes.append(hihat)

# Bar 1-4: Bass (Marcus)
def create_bass():
    bass_program = 33  # Electric Bass
    bass_inst = Instrument(program=bass_program)
    pm.instruments.append(bass_inst)

    # Dm7 walking line with chromatic approaches
    # Bar 1: D, C, D, F
    # Bar 2: A, G, A, B
    # Bar 3: D, C, D, F
    # Bar 4: A, G, A, Dm7
    bass_notes = [
        # Bar 1
        Note(40, 0, beat_to_sec(0), beat_to_sec(0) + 0.25),  # D2
        Note(39, 0, beat_to_sec(0.5), beat_to_sec(0.5) + 0.25),  # C2
        Note(40, 0, beat_to_sec(1), beat_to_sec(1) + 0.25),  # D2
        Note(42, 0, beat_to_sec(1.5), beat_to_sec(1.5) + 0.25),  # F2

        # Bar 2
        Note(44, 0, beat_to_sec(2), beat_to_sec(2) + 0.25),  # A2
        Note(43, 0, beat_to_sec(2.5), beat_to_sec(2.5) + 0.25),  # G2
        Note(44, 0, beat_to_sec(3), beat_to_sec(3) + 0.25),  # A2
        Note(45, 0, beat_to_sec(3.5), beat_to_sec(3.5) + 0.25),  # B2

        # Bar 3
        Note(40, 0, beat_to_sec(4), beat_to_sec(4) + 0.25),  # D2
        Note(39, 0, beat_to_sec(4.5), beat_to_sec(4.5) + 0.25),  # C2
        Note(40, 0, beat_to_sec(5), beat_to_sec(5) + 0.25),  # D2
        Note(42, 0, beat_to_sec(5.5), beat_to_sec(5.5) + 0.25),  # F2

        # Bar 4
        Note(44, 0, beat_to_sec(6), beat_to_sec(6) + 0.25),  # A2
        Note(43, 0, beat_to_sec(6.5), beat_to_sec(6.5) + 0.25),  # G2
        Note(44, 0, beat_to_sec(7), beat_to_sec(7) + 0.25),  # A2
        Note(41, 0, beat_to_sec(7.5), beat_to_sec(7.5) + 0.25),  # D2 (final note)
    ]
    for note in bass_notes:
        bass_inst.notes.append(note)

# Bar 2-4: Piano (Diane)
def create_piano():
    piano_program = 0  # Acoustic Piano
    piano_inst = Instrument(program=piano_program)
    pm.instruments.append(piano_inst)

    # Bar 2: Gm7 - comp on 2 and 4
    # Gm7: G, B♭, D, F
    # Open voicing: G, B♭, D, F (spaced out)
    note1 = Note(67, 0, beat_to_sec(1), beat_to_sec(1) + 0.05)
    note2 = Note(62, 0, beat_to_sec(1), beat_to_sec(1) + 0.05)
    note3 = Note(64, 0, beat_to_sec(1), beat_to_sec(1) + 0.05)
    note4 = Note(66, 0, beat_to_sec(1), beat_to_sec(1) + 0.05)
    piano_inst.notes.extend([note1, note2, note3, note4])

    # Bar 3: Cm7 - comp on 2 and 4
    # Cm7: C, E♭, G, B♭
    note1 = Note(60, 0, beat_to_sec(2.5), beat_to_sec(2.5) + 0.05)
    note2 = Note(57, 0, beat_to_sec(2.5), beat_to_sec(2.5) + 0.05)
    note3 = Note(67, 0, beat_to_sec(2.5), beat_to_sec(2.5) + 0.05)
    note4 = Note(62, 0, beat_to_sec(2.5), beat_to_sec(2.5) + 0.05)
    piano_inst.notes.extend([note1, note2, note3, note4])

    # Bar 4: F7 - comp on 2 and 4
    # F7: F, A, C, E
    note1 = Note(65, 0, beat_to_sec(4), beat_to_sec(4) + 0.05)
    note2 = Note(68, 0, beat_to_sec(4), beat_to_sec(4) + 0.05)
    note3 = Note(67, 0, beat_to_sec(4), beat_to_sec(4) + 0.05)
    note4 = Note(69, 0, beat_to_sec(4), beat_to_sec(4) + 0.05)
    piano_inst.notes.extend([note1, note2, note3, note4])

# Bar 2-4: Tenor Sax (You)
def create_sax():
    sax_program = 64  # Tenor Sax
    sax_inst = Instrument(program=sax_program)
    pm.instruments.append(sax_inst)

    # Motif: D (40), E♭ (41), D (40), F (42) — simple, singable, with space
    # Bar 2: E♭ (41) to F (42)
    note1 = Note(41, 0, beat_to_sec(1), beat_to_sec(1) + 0.25)
    note2 = Note(42, 0, beat_to_sec(1.5), beat_to_sec(1.5) + 0.25)

    # Bar 3: Repeat last two notes
    note3 = Note(41, 0, beat_to_sec(2.5), beat_to_sec(2.5) + 0.25)
    note4 = Note(42, 0, beat_to_sec(3), beat_to_sec(3) + 0.25)

    # Bar 4: Repeat
    note5 = Note(41, 0, beat_to_sec(4), beat_to_sec(4) + 0.25)
    note6 = Note(42, 0, beat_to_sec(4.5), beat_to_sec(4.5) + 0.25)

    sax_inst.notes.extend([note1, note2, note3, note4, note5, note6])

# Create all instruments
create_drums()
create_bass()
create_piano()
create_sax()

# Save the MIDI
pm.write("Dante_Intro.mid")
print("MIDI file saved as 'Dante_Intro.mid'.")
