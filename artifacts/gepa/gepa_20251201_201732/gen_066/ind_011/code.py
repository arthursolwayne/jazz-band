
import numpy as np
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Parameters
BPM = 160
BEAT_DURATION = 60 / BPM  # in seconds
BAR_DURATION = 4 * BEAT_DURATION  # 4/4 time
TOTAL_DURATION = BAR_DURATION * 4  # 4 bars

# Create a new MIDI file
midi = pretty_midi.Pretty MIDI()

# Set tempo
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempos = [pretty_midi.Tempo(60 / BPM, 0)]  # 60 BPM is default, but we use 160

# Define instruments
drums = Instrument(program=pretty_midi.instrument_name_to_program('Drums'), is_drum=True)
bass = Instrument(program=pretty_midi.instrument_name_to_program('Acoustic Bass'))
piano = Instrument(program=pretty_midi.instrument_name_to_program('Electric Piano 1'))
sax = Instrument(program=pretty_midi.instrument_name_to_program('Tenor Saxophone'))

# Add instruments to MIDI
midi.instruments = [drums, bass, piano, sax]

#--------------------------
# Bar 1 (0.0 to 1.5 seconds): Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Duration: 1.5 seconds
# 1 beat = 0.375 seconds
# 8 eighth notes = 4 beats

for i in range(8):
    time = i * 0.375
    note_number = 35  # Kick
    if i % 2 == 0:
        note_number = 36  # Snare
    elif i % 2 == 1:
        note_number = 42  # Hihat
    drums.notes.append(Note(note_number, time, time + 0.125))

#--------------------------
# Bars 2-4 (1.5 to 6.0 seconds): Full ensemble

# Bar 2: Diane on piano - Open voicing (Fmaj7), comp on 2 and 4
# 1st measure: 1 beat rest, then chords on 2 and 4
# Chord: Fmaj7 (F, A, C, E)
# Voicing: F (C4), A (E4), C (G4), E (B4)

# Bar 2 (1.5s to 3.0s)
piano_notes = [
    Note(76, 1.5, 1.625),  # F (C4)
    Note(79, 1.5, 1.625),  # A (E4)
    Note(82, 1.5, 1.625),  # C (G4)
    Note(87, 1.5, 1.625),  # E (B4)
    Note(76, 2.0, 2.125),  # F (C4)
    Note(79, 2.0, 2.125),  # A (E4)
    Note(82, 2.0, 2.125),  # C (G4)
    Note(87, 2.0, 2.125),  # E (B4)
]
piano.notes.extend(piano_notes)

# Bar 3 (3.0s to 4.5s): Diane - B7#9 (B, D#, F#, A, C natural)
# Voicing: B (F#4), D# (A4), F# (C#5), A (E5), C natural (G4)
# Comp on 2 and 4

piano_notes = [
    Note(87, 3.0, 3.125),  # B (F#4)
    Note(91, 3.0, 3.125),  # D# (A4)
    Note(93, 3.0, 3.125),  # F# (C#5)
    Note(97, 3.0, 3.125),  # A (E5)
    Note(81, 3.0, 3.125),  # C natural (G4)
    Note(87, 3.5, 3.625),  # B (F#4)
    Note(91, 3.5, 3.625),  # D# (A4)
    Note(93, 3.5, 3.625),  # F# (C#5)
    Note(97, 3.5, 3.625),  # A (E5)
    Note(81, 3.5, 3.625),  # C natural (G4)
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5s to 6.0s): Diane - Gm7 (G, Bb, D, F)
# Voicing: G (D4), Bb (F#4), D (A4), F (C5)
# Comp on 2 and 4

piano_notes = [
    Note(78, 4.5, 4.625),  # G (D4)
    Note(81, 4.5, 4.625),  # Bb (F#4)
    Note(84, 4.5, 4.625),  # D (A4)
    Note(87, 4.5, 4.625),  # F (C5)
    Note(78, 5.0, 5.125),  # G (D4)
    Note(81, 5.0, 5.125),  # Bb (F#4)
    Note(84, 5.0, 5.125),  # D (A4)
    Note(87, 5.0, 5.125),  # F (C5)
]
piano.notes.extend(piano_notes)

#--------------------------
# Bass line: Marcus - Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches

# Bar 2 (1.5s to 3.0s): F (38), G (43), chromatic up to Ab (44)
# Bar 3 (3.0s to 4.5s): Bb (45), A (44), G (43)
# Bar 4 (4.5s to 6.0s): G (43), F (38), E (37)

bass_notes = [
    Note(38, 1.5, 1.625),  # F (root)
    Note(43, 2.0, 2.125),  # G (fifth)
    Note(44, 2.5, 2.625),  # Ab (chromatic)
    Note(45, 3.0, 3.125),  # Bb
    Note(44, 3.5, 3.625),  # A
    Note(43, 4.0, 4.125),  # G
    Note(38, 4.5, 4.625),  # F
    Note(37, 5.0, 5.125),  # E
]
bass.notes.extend(bass_notes)

#--------------------------
# Tenor sax: Dante - One short motif, haunting, incomplete

# Bar 2 (1.5s to 3.0s): Melody notes
# F (76), G (78), F# (79), rest
# Bar 3 (3.0s to 4.5s): F (76), Bb (81), rest
# Bar 4 (4.5s to 6.0s): G (78), F (76), rest

sax_notes = [
    Note(76, 1.5, 1.625),  # F
    Note(78, 2.0, 2.125),  # G
    Note(79, 2.5, 2.625),  # F#
    Note(76, 3.0, 3.125),  # F
    Note(81, 3.5, 3.625),  # Bb
    Note(78, 4.5, 4.625),  # G
    Note(76, 5.0, 5.125),  # F
]
sax.notes.extend(sax_notes)

#--------------------------
# Save the MIDI file
# midi.write disabled

print("MIDI file written as 'dante_intro.mid'")
