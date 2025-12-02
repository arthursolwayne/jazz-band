
import pretty_midi
from pretty_midi import Note, Instrument, TimeSignature, KeySignature

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [TimeSignature(numerator=4, denominator=4, time=0.0,螃蟹=120.0)]
midi.key_signature_changes = [KeySignature(key_number=21, time=0.0)]  # F minor (key_number 21)

# Set tempo
midi.initial_tempo = 160  # 160 BPM

# Instrument instruments
drums = Instrument(program=0, is_drum=True, name='Drums')
bass = Instrument(program=33, name='Bass')
piano = Instrument(program=0, name='Piano')
sax = Instrument(program=64, name='Saxophone')

# Time per bar = 1.5 seconds (at 160 BPM, 60 / 160 * 4 = 1.5)
bar_length = 1.5
note_duration = bar_length / 8  # 8th note

# Bar 1: Drums only - Setup with tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    Note(36, 0.0, note_duration),  # Kick on 1
    Note(38, 0.375, note_duration),  # Snare on 2
    Note(42, 0.75, note_duration),  # Hihat on 3
    Note(36, 1.125, note_duration),  # Kick on 3
    Note(38, 1.5, note_duration),  # Snare on 4
    Note(42, 0.0, note_duration),  # Hihat on 1
    Note(42, 0.375, note_duration),  # Hihat on 2
    Note(42, 0.75, note_duration),  # Hihat on 3
    Note(42, 1.125, note_duration),  # Hihat on 4
    Note(42, 1.5, note_duration)  # Hihat on 4 (end)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in. Sax melody
# F minor scale: F, Gb, Ab, Bb, B, Db, Eb, F
# Motif: F -> Ab -> Bb -> F (octave up)
# Start on 0.0, end at 0.75, then leave it hanging

sax_notes = [
    Note(71, 0.0, note_duration),  # F (octave 4)
    Note(76, 0.375, note_duration),  # Ab
    Note(74, 0.75, note_duration),  # Bb
    Note(71, 0.75, note_duration * 2),  # F (hold for rest of bar)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F minor
# Fm7 -> Bbm7 -> Ebm7 -> Abm7 (II-V-i progression in Fm)
# Chromatic approach: F -> Eb -> F -> Gb (approach F)
# Then walking line: F, Gb, Ab, Bb, B, Db, Eb, F

bass_notes = [
    Note(53, 0.0, note_duration * 2),  # F
    Note(51, 0.375, note_duration),  # Eb
    Note(53, 0.75, note_duration),  # F
    Note(54, 1.125, note_duration),  # Gb
    Note(56, 1.5, note_duration),  # Ab
    Note(57, 1.875, note_duration),  # Bb
    Note(58, 2.25, note_duration),  # B
    Note(55, 2.625, note_duration),  # Db
    Note(53, 3.0, note_duration),  # Eb
    Note(53, 3.375, note_duration),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 2: Fm7 on 2 and 4
# Fm7 = F, Ab, Bb, Db
# Play on beat 2 and 4

piano_notes = [
    Note(71, 0.375, note_duration * 2),  # F
    Note(76, 0.375, note_duration * 2),  # Ab
    Note(74, 0.375, note_duration * 2),  # Bb
    Note(67, 0.375, note_duration * 2),  # Db
    Note(71, 1.5, note_duration * 2),  # F
    Note(76, 1.5, note_duration * 2),  # Ab
    Note(74, 1.5, note_duration * 2),  # Bb
    Note(67, 1.5, note_duration * 2),  # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Save the MIDI file
midi.write('fm_intro.mid')
print("MIDI file generated: fm_intro.mid")
