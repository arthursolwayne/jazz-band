
import pretty_midi
from pretty_midi import Note, Instrument, TimeSignature, KeySignature

# Create a MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature and key signature
pm.time_signature_changes = [TimeSignature(numerator=4, denominator=4, time=0.0)]
pm.key_signature_changes = [KeySignature(key_number=2, time=0.0)]  # D major

# Create instruments
drums = Instrument(program=10, is_drum=True, name="Drums")
piano = Instrument(program=0, name="Piano")
bass = Instrument(program=33, name="Bass")
sax = Instrument(program=64, name="Saxophone")

pm.instruments = [drums, piano, bass, sax]

# --- DRUMS (Little Ray) ---
# Bar 1: Hi-hat pattern with tension and space
drum_notes = [
    Note(velocity=100, pitch=42, start=0.0, end=0.1875),  # Hi-hat on 1
    Note(velocity=100, pitch=42, start=0.375, end=0.5625), # Hi-hat on 2
    Note(velocity=100, pitch=42, start=0.75, end=0.9375),  # Hi-hat on 3
    Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hi-hat on 4
]

# Bar 2-4: Full drums
for bar in range(2, 5):
    start = (bar - 1) * 1.5  # bar 2 starts at 1.5s, bar 3 at 3.0s, bar 4 at 4.5s
    # Kick on 1
    Note(velocity=110, pitch=36, start=start + 0.0, end=start + 0.1875).add_to_instrument(drums)
    # Snare on 2
    Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.5625).add_to_instrument(drums)
    # Kick on 3
    Note(velocity=110, pitch=36, start=start + 0.75, end=start + 0.9375).add_to_instrument(drums)
    # Snare on 4
    Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.3125).add_to_instrument(drums)
    # Hi-hat on every eighth
    for i in range(0, 8):
        Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875).add_to_instrument(drums)

# --- PIANO (Diane) ---
# Bar 2: 7th chords on 2 and 4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # 2nd beat (7th chord)
    Note(velocity=90, pitch=74, start=start + 0.375, end=start + 0.4375).add_to_instrument(piano)  # D7 (D, F#, A, C)
    Note(velocity=80, pitch=76, start=start + 0.375, end=start + 0.4375).add_to_instrument(piano)  # F#
    Note(velocity=90, pitch=79, start=start + 0.375, end=start + 0.4375).add_to_instrument(piano)  # A
    Note(velocity=80, pitch=71, start=start + 0.375, end=start + 0.4375).add_to_instrument(piano)  # C
    # 4th beat (7th chord)
    Note(velocity=90, pitch=74, start=start + 1.125, end=start + 1.1875).add_to_instrument(piano)
    Note(velocity=80, pitch=76, start=start + 1.125, end=start + 1.1875).add_to_instrument(piano)
    Note(velocity=90, pitch=79, start=start + 1.125, end=start + 1.1875).add_to_instrument(piano)
    Note(velocity=80, pitch=71, start=start + 1.125, end=start + 1.1875).add_to_instrument(piano)

# --- BASS (Marcus) ---
# Chromatic walking line, no repeated notes
bass_notes = [62, 63, 61, 62, 64, 63, 65, 64, 63, 62, 61, 62, 64, 63, 65, 64]
for note in bass_notes:
    start = (bass_notes.index(note) / 8) * 1.5
    end = start + 0.1875
    Note(velocity=90, pitch=note, start=start, end=end).add_to_instrument(bass)

# --- SAX (You) ---
# Bar 2: Start the motif
start = 1.5
sax_notes = [
    Note(velocity=100, pitch=62, start=start, end=start + 0.75),  # D4, long note
    Note(velocity=100, pitch=65, start=start + 1.0, end=start + 1.25),  # F#4
    Note(velocity=100, pitch=64, start=start + 1.5, end=start + 1.75),  # G4
    Note(velocity=100, pitch=62, start=start + 2.25, end=start + 2.5),  # D4
    Note(velocity=100, pitch=67, start=start + 2.5, end=start + 2.75),  # B4
    Note(velocity=100, pitch=62, start=start + 3.0, end=start + 3.25),  # D4
    Note(velocity=100, pitch=65, start=start + 3.25, end=start + 3.5),  # F#4
    Note(velocity=100, pitch=64, start=start + 3.75, end=start + 4.0),  # G4
    Note(velocity=100, pitch=66, start=start + 4.0, end=start + 4.25),  # A4
    Note(velocity=100, pitch=67, start=start + 4.5, end=start + 4.75),  # B4
    Note(velocity=100, pitch=62, start=start + 5.0, end=start + 5.25),  # D4
    Note(velocity=100, pitch=65, start=start + 5.25, end=start + 5.5),  # F#4
    Note(velocity=100, pitch=64, start=start + 5.75, end=start + 6.0),  # G4
]

for note in sax_notes:
    note.add_to_instrument(sax)

# Write the MIDI file
pm.write('jazz_intro.mid')
print("Generated 'jazz_intro.mid' — 4 bars in D major, 160 BPM.")
